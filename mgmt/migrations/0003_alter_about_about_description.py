# Generated by Django 4.2 on 2024-01-04 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mgmt", "0002_alter_about_options_alter_about_about_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="about",
            name="about_description",
            field=models.TextField(max_length=50000),
        ),
    ]