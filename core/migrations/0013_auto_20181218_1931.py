# Generated by Django 2.1.3 on 2018-12-18 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20181218_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='static/imagens/eventos'),
        ),
    ]
