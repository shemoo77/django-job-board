# Generated by Django 5.1.7 on 2025-03-19 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0002_job_job_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="describtion",
            field=models.TextField(default="", max_length=1000),
            preserve_default=False,
        ),
    ]
