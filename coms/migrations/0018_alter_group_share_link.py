# Generated by Django 4.1.1 on 2022-10-10 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("coms", "0017_alter_group_files_alter_group_share_link_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="share_link",
            field=models.URLField(
                blank=True,
                default="http://127.0.0.1:8000/api/group/<django.db.models.fields.UUIDField>/join/",
            ),
        ),
    ]
