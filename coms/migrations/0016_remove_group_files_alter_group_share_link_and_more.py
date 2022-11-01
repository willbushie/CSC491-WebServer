# Generated by Django 4.1.1 on 2022-10-10 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("coms", "0015_user_username_alter_user_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="group",
            name="files",
        ),
        migrations.AlterField(
            model_name="group",
            name="share_link",
            field=models.URLField(
                blank=True,
                default="http://127.0.0.1:8000/api/group/<django.db.models.fields.UUIDField>/join/",
                null=True,
            ),
        ),
        migrations.RemoveField(
            model_name="group",
            name="users",
        ),
        migrations.AddField(
            model_name="group",
            name="files",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="coms.file",
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="users",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="coms.user",
            ),
        ),
    ]