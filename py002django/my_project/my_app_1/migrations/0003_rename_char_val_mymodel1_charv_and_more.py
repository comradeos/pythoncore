# Generated by Django 4.0.3 on 2022-10-19 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app_1', '0002_rename_mymodel_mymodel1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymodel1',
            old_name='char_val',
            new_name='charv',
        ),
        migrations.RenameField(
            model_name='mymodel1',
            old_name='int_val',
            new_name='intv',
        ),
    ]