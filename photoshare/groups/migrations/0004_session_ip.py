# Generated by Django 4.1.3 on 2022-12-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0003_alter_file_created_alter_group_end_alter_group_start"),
    ]

    operations = [
        migrations.AddField(
            model_name="session",
            name="ip",
            field=models.GenericIPAddressField(default="0.0.0.0"),
        ),
    ]
