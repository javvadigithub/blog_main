# Generated by Django 4.2 on 2024-01-07 05:35

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0008_alter_blog_blog_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="blog_body",
            field=django_summernote.fields.SummernoteTextField(blank=True, null=True),
        ),
    ]
