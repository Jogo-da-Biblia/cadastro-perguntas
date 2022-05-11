from app.biblia.models import Livro, Versiculo
from app.core.models import User
from django.db import models


class Tema(models.Model):
    nome = models.CharField(max_length=50)
    cor = models.CharField(max_length=6)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tema'


class Pergunta(models.Model):

    TIPO_RESPOSTA = [
        ('MES', 'Múltipla Escolha'),
        ('RCO', 'Referência Completa'),
        ('RLC', 'Referência Livro-Capítulo'),
        ('RES', 'Resposta Simples')
    ]

    id = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(
        'Grupo', related_name='grupo', on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    enunciado = models.TextField()
    tipo_resposta = models.CharField(
        max_length=3, choices=TIPO_RESPOSTA, verbose_name='Tipo de Resposta')
    refencia_resposta = models.ForeignKey(
        'Referencia', on_delete=models.CASCADE,
        related_name='referencia_resposta')
    outras_referencias = models.ForeignKey(
        'Referencia', on_delete=models.CASCADE)
    status = models.BooleanField(default=True, verbose_name='Pergunta Status')
    criado_por = models.ForeignKey(
        User, related_name='criado_por', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    revisado_por = models.ForeignKey(
        User, related_name='revisado_por', on_delete=models.CASCADE)
    revisado_em = models.DateTimeField(auto_now_add=True)
    publicado_por = models.ForeignKey(
        User, related_name='publicado_por', on_delete=models.CASCADE)
    publicado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.enunciado

    class Meta:
        db_table = 'pergunta'
        verbose_name = 'Pergunta'


class Referencia(models.Model):
    id = models.AutoField(primary_key=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    versiculo = models.ForeignKey(Versiculo, on_delete=models.CASCADE,
                                  verbose_name='Versículo')

    def __str__(self):
        return f"{self.livro} {self.versiculo}"

    class Meta:
        db_table = 'referencia'


class Alternativa(models.Model):
    texto = models.TextField()
    pergunta = models.ForeignKey(Pergunta, related_name='alternativas',
                                 on_delete=models.CASCADE)
    # Marca se essa é uma das respostas corretas ou é uma falsa
    resposta_certa = models.BooleanField(default=False)

    def __str__(self):
        return self.texto

    class Meta:
        db_table = 'alternativa'


class Comentario(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    email = models.CharField(max_length=126)
    phone = models.CharField(max_length=11)
    is_whatsapp = models.BooleanField('É Whatsapp?', default=True)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.mensagem} - {self.email}'

    class Meta:
        db_table = 'comentario'


class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    cor = models.CharField(max_length=6)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'grupo'
        verbose_name = 'Grupo'
