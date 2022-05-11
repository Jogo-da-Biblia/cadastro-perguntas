from app.perguntas.models import Pergunta, Alternativa, Referencia
from django.contrib import admin
from django.core.exceptions import ValidationError
'''
Permissões:
COLABORADOR: quem manda comentários, criticas e perguntas
REVISOR: quem revisa as perguntas e 
PUBLICADOR
'''


class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 1


class ReferenciaInline(admin.TabularInline):
    model = Referencia
    extra = 1


class PerguntaAdmin(admin.ModelAdmin):
    fields = ('tema', 'enunciado', 'tipo_resposta',
              'criado_por', 'status')
    inlines = [AlternativaInline]

    def add_view(self, request, form_url='', extra_context=None):
        try:
            return super(PerguntaAdmin, self).add_view(
                request, form_url, extra_context
            )
        except ValidationError as e:
            print(e)

    # def get_changeform_initial_data(self, request):
    #     get_data = super(PerguntaAdmin, self).get_changeform_initial_data(request)
    #     get_data['criado_por'] = request.user.id
    #     return get_data

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.has_perm('review_question'):
            return qs
        # Filtrar apenas que ainda não tenham sido revisadas
        return qs.filter(criado_por=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "criado_por":
            kwargs["initial"] = request.user.id
            kwargs["disabled"] = True
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def change_view(self, request, object_id, extra_context=None):
        if request.user.has_perm('review_question'):
            self.fields.append('revisado_por')
            self.fields.append('revisado_em')
            self.readonly_fields.append('revisado_por')
            self.readonly_fields.append('revisado_em')
        if request.user.has_perm('publish_question'):
            self.fields.append('publicado_por')
            self.fields.append('publicado_em')
            # self.readonly_fields = ('revisado_por','revisado_em')

    def save_model(self, request, obj, form, change):
        # Se quem salvou é PUBLICADOR, então ele ganha o publicado_em e publicado_por
        obj.user = request.user
        super().save_model(request, obj, form, change)

# Desabilitando a tela de Adicionar principalmente para o colaborador não se confundir


class AlternativaAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Alternativa, AlternativaAdmin)
