# Generated by Django 4.0.4 on 2022-06-01 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_evento_usuario_alter_evento_data_criacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local_evento',
            field=models.TextField(blank=True, null=True),
        ),
    ]
