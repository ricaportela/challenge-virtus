# Generated by Django 2.0.4 on 2018-04-18 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180418_1151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='nome_razao_social',
            new_name='nomerazaosocial',
        ),
    ]