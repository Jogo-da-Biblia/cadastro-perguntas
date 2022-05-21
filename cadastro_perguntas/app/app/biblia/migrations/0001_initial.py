# Generated by Django 3.1.14 on 2022-05-21 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicao', models.IntegerField()),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Testamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='Versao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=33)),
            ],
            options={
                'verbose_name': 'Versão',
                'verbose_name_plural': 'Versões',
            },
        ),
        migrations.CreateModel(
            name='Versiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capitulo', models.IntegerField()),
                ('versiculo', models.IntegerField()),
                ('texto', models.TextField()),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versiculos', to='biblia.livro')),
                ('versao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versiculos', to='biblia.versao')),
            ],
            options={
                'verbose_name': 'Versículo',
            },
        ),
        migrations.AddField(
            model_name='livro',
            name='testamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='biblia.testamento'),
        ),
    ]
