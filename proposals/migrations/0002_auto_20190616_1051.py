# Generated by Django 2.2 on 2019-06-16 10:51

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposals',
            name='current_urls',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='proposals',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='proposals',
            name='pre_requisites',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='proposals',
            name='speaker_info',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='proposals',
            name='speaker_links',
            field=tinymce.models.HTMLField(),
        ),
    ]
