# Generated by Django 3.2.16 on 2023-02-11 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0004_data_migration"),
    ]

    operations = [
        migrations.RenameField(
            model_name="courseteachers",
            old_name="cource",
            new_name="course",
        ),
    ]
