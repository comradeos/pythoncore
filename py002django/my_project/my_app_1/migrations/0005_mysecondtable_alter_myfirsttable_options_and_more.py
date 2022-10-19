# Generated by Django 4.0.3 on 2022-10-19 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app_1', '0004_rename_mymodel1_myfirsttable'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySecondTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'MySecondTable',
            },
        ),
        migrations.AlterModelOptions(
            name='myfirsttable',
            options={'verbose_name_plural': 'MyFirstTable'},
        ),
        migrations.AddField(
            model_name='myfirsttable',
            name='fork',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app_1.mysecondtable'),
        ),
    ]
