# Generated by Django 3.2.6 on 2021-10-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apprestaurante', '0004_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='font_size',
            field=models.IntegerField(),
        ),
    ]
