# Generated by Django 2.2.12 on 2020-05-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_remove_customtext_hgfghfh"),
    ]

    operations = [
        migrations.CreateModel(
            name="Test",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hjgjh", models.BigIntegerField()),
            ],
        ),
    ]
