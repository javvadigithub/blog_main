# Generated by Django 4.2 on 2024-01-06 16:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0006_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="blog_body",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
