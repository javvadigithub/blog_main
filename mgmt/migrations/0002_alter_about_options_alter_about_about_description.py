# Generated by Django 4.2 on 2024-01-04 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mgmt", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="about",
            options={"verbose_name_plural": "About"},
        ),
        migrations.AlterField(
            model_name="about",
            name="about_description",
            field=models.TextField(max_length=5000),
        ),
    ]
