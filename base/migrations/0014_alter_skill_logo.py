# Generated by Django 4.1.2 on 2022-10-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_skill_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='logo',
            field=models.ImageField(default='skill.png', null=True, upload_to=''),
        ),
    ]
