from django.forms import BaseInlineFormSet, inlineformset_factory, formset_factory
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, UpdateView, CreateView

from app.perguntas.models import Pergunta, Alternativa
from app.perguntas.forms import AlternativaForm
from app.biblia.models import Versiculo, Livro
from app.biblia.forms import ReferenciaForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class PerguntasPageView(ListView):
    model = Pergunta

    def get_queryset(self):
        return Pergunta.objects.filter(criado_por=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["alternativas"] = Alternativa.objects.all()
        return context


class PerguntaCreateView(CreateView, BaseInlineFormSet):
    model = Pergunta
    template_name = 'perguntas/pergunta_add.html'
    fields = ['tema', 'enunciado', 'tipo_resposta']
    success_url = '/'

    def form_valid(self, form):
        form.instance.criado_por = self.request.user

        AlternativasFormSet = inlineformset_factory(Pergunta, Alternativa, form=AlternativaForm)
        if self.request.method == 'POST':
            formset = AlternativasFormSet(self.request.POST, instance=form.instance)
            if formset.is_valid() and form.is_valid():
                form.save()
                formset.save()

        # ReferenciaFormSet = formset_factory(Pergunta, Versiculo, form=ReferenciaForm)
        # if self.request.method == 'POST':
        #     formset = ReferenciaFormSet(self.request.POST, instance=form.instance)
        #     print(formset)
        #     if formset.is_valid() and form.is_valid():
        #         form.save()
        #         formset.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["versiculos"] = Versiculo.objects.all()
        context["livros"] = Livro.objects.all()

        AlternativasFormSet = inlineformset_factory(Pergunta, Alternativa, form=AlternativaForm, extra=1, can_delete=True)
        context["formset"] = AlternativasFormSet()
        return context


class PerguntaUpdateView(UpdateView):
    model = Pergunta
    fields = ['tema', 'enunciado', 'tipo_resposta']
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        AlternativasFormSet = inlineformset_factory(Pergunta, Alternativa, form=AlternativaForm, extra=0, can_delete=True)
        context["formset"] = AlternativasFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        AlternativasFormSet = inlineformset_factory(Pergunta, Alternativa, form=AlternativaForm)
        if self.request.method == 'POST':
            formset = AlternativasFormSet(self.request.POST, instance=form.instance)
            if formset.is_valid():
                formset.save()

        return super().form_valid(form)


def get_capitulos(request):
    if request.method == 'POST':
        capitulos = Versiculo.objects.filter(livro_id=request.POST['livro'])
        return JsonResponse(list(capitulos.values()), safe=False)


def get_versiculos(request):
    if request.method == 'POST':
        capitulos = Versiculo.objects.filter(livro_id=request.POST['livro'])
        versiculos = capitulos.filter(capitulo=request.POST['capitulo'])
        return JsonResponse(list(versiculos.values()), safe=False)


def get_texto_biblico(request):
    if request.method == 'POST':
        capitulos = Versiculo.objects.filter(livro_id=request.POST['livro'])
        versiculos = capitulos.filter(capitulo=request.POST['capitulo'])
        texto_biblico = versiculos.filter(versiculo=request.POST['versiculo'])
        return JsonResponse(texto_biblico.last().texto, safe=False)
