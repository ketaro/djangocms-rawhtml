# Generated by Django 3.2.16 on 2022-12-16 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_rawhtml', '0001_rawhtmlplugindata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawhtmlplugindata',
            name='body',
            field=models.TextField(verbose_name='HTML'),
        ),
        migrations.AlterField(
            model_name='rawhtmlplugindata',
            name='label',
            field=models.CharField(default='', max_length=40),
        ),
    ]
