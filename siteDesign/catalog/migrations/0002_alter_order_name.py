# Generated by Django 3.2.16 on 2022-10-25 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=254, verbose_name='Название'),
        ),
    ]
