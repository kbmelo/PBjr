# Generated by Django 2.1.3 on 2018-12-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20181214_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresasJuniores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=200)),
                ('logoEmpresa', models.ImageField(blank=True, upload_to='static/imagens/empresasJuniores')),
                ('descricaoEmpresa', models.CharField(max_length=200)),
                ('localEmpresa', models.CharField(max_length=200)),
                ('siteEmpresa', models.CharField(max_length=200)),
                ('emailEmpresa', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.RenameField(
            model_name='parceiro',
            old_name='imagem',
            new_name='logoEmpresa',
        ),
        migrations.AlterField(
            model_name='parceiro',
            name='nome',
            field=models.CharField(default='', max_length=200),
        ),
    ]