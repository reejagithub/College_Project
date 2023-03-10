# Generated by Django 4.1.6 on 2023-03-03 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("collegeapp", "0002_remove_course_duration"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("stud_name", models.CharField(max_length=255)),
                ("stud_address", models.CharField(max_length=255)),
                ("stud_age", models.IntegerField(blank=True, default=None, null=True)),
                ("join_date", models.DateField()),
                (
                    "course",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="collegeapp.course",
                    ),
                ),
            ],
        ),
    ]
