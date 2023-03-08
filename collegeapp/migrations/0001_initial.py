# Generated by Django 4.1.6 on 2023-03-02 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("course_name", models.CharField(max_length=100)),
                ("fee", models.IntegerField(default=0)),
                ("duration", models.DurationField()),
            ],
        ),
    ]
