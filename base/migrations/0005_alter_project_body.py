# Generated by Django 4.1.2 on 2022-10-16 03:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_skill_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
