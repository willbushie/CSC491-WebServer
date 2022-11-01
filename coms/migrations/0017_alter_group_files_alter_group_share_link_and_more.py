# Generated by Django 4.1.1 on 2022-10-10 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("coms", "0016_remove_group_files_alter_group_share_link_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="files",
            field=models.ForeignKey(
                blank=True, on_delete=django.db.models.deletion.CASCADE, to="coms.file"
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="share_link",
            field=models.URLField(
                blank=True,
                default="http://127.0.0.1:8000/api/group/<bound method UUIDField.to_python of <django.db.models.fields.UUIDField>>/join/",
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="users",
            field=models.ForeignKey(
                blank=True, on_delete=django.db.models.deletion.CASCADE, to="coms.user"
            ),
        ),
    ]
