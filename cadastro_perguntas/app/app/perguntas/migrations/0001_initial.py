# Generated by Django 3.1.14 on 2022-06-16 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('biblia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Referencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblia.livro')),
                ('versiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblia.versiculo', verbose_name='Versículo')),
            ],
            options={
                'verbose_name': 'Referência',
                'verbose_name_plural': 'Referências',
            },
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('enunciado', models.TextField()),
                ('tipo_resposta', models.CharField(choices=[('MES', 'Múltipla Escolha'), ('RCO', 'Referência Completa'), ('RLC', 'Referência Livro-Capítulo'), ('RES', 'Resposta Simples')], max_length=3, verbose_name='Tipo de Resposta')),
                ('outras_referencias', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(default=False, verbose_name='Publicado')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('revisado_status', models.BooleanField(default=False, verbose_name='Revisado')),
                ('revisado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('publicado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('criado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criado_por', to=settings.AUTH_USER_MODEL)),
                ('publicado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publicado_por', to=settings.AUTH_USER_MODEL)),
                ('refencia_resposta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perguntas.referencia')),
                ('revisado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revisado_por', to=settings.AUTH_USER_MODEL)),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perguntas.tema')),
            ],
            options={
                'verbose_name': 'Pergunta',
            },
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('texto', models.TextField()),
                ('alternativas_corretas', models.BooleanField(default=False)),
                ('alternativas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternativas', to='perguntas.pergunta')),
            ],
        ),
    ]
