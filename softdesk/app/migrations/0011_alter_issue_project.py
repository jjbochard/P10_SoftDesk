# Generated by Django 4.0.2 on 2022-07-24 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_alter_comment_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issue",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="issues",
                to="app.project",
            ),
        ),
    ]
