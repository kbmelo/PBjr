# Generated by Django 2.1.3 on 2019-02-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_evento_dataevento'),
    ]

    operations = [
        migrations.CreateModel(
            name='MVV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('missao', models.TextField(default='', max_length=200, verbose_name='Missão')),
                ('visao', models.TextField(default='', max_length=200, verbose_name='Visão')),
                ('valor_1', models.CharField(blank=True, max_length=40, verbose_name='Valor(opcional)')),
                ('valor_2', models.CharField(blank=True, max_length=40, verbose_name='Valor(opcional)')),
                ('valor_3', models.CharField(blank=True, max_length=40, verbose_name='Valor(opcional)')),
                ('valor_4', models.CharField(blank=True, max_length=255, verbose_name='Valor(opcional)')),
                ('valor_5', models.CharField(blank=True, max_length=40, verbose_name='Valor(opcional)')),
                ('valor_6', models.CharField(blank=True, max_length=40, verbose_name='Valor(opcional)')),
            ],
            options={
                'verbose_name': 'Missão, Visão, Valores',
            },
        ),
    ]
