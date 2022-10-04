# Generated by Django 4.1.1 on 2022-10-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("coms", "0010_group_creation_group_last_updated"),
    ]

    operations = [
        migrations.RenameField(
            model_name="group",
            old_name="members",
            new_name="users",
        ),
        migrations.AddField(
            model_name="group",
            name="active",
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name="group",
            name="share_link",
            field=models.URLField(blank=True),
        ),
    ]
