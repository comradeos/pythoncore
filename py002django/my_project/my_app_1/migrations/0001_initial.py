# Generated by Django 4.0.3 on 2022-10-19 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_val', models.IntegerField()),
                ('char_val', models.CharField(max_length=255)),
            ],
        ),
    ]
