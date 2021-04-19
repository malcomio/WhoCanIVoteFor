# Generated by Django 2.2.18 on 2021-03-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parties", "0009_manifesto_easy_read_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="localparty",
            name="is_local",
            field=models.BooleanField(
                default=True,
                help_text="Used to identify if obj is related to a local election",
            ),
        ),
    ]