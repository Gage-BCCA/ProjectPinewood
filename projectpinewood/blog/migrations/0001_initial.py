# Generated by Django 5.1.7 on 2025-03-14 00:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PostStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("subtitle", models.CharField(max_length=255)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_published", models.DateTimeField(default=None, null=True)),
                ("date_last_modified", models.DateTimeField(auto_now=True)),
                ("body", models.TextField()),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("featured_image", models.TextField(null=True)),
                ("view_count", models.BigIntegerField(default=0)),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.poststatus",
                    ),
                ),
            ],
        ),
    ]
