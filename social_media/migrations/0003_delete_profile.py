# Generated by Django 4.2.1 on 2023-06-06 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0002_alter_category_options_alter_post_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
