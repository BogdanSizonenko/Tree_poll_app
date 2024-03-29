# Generated by Django 5.0 on 2024-02-07 16:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("poll", "0011_remove_question_event_trigger_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="choice_trigger",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    blank=True,
                    max_length=20,
                    null=True,
                    verbose_name="Номер триггер вопроса",
                ),
                blank=True,
                null=True,
                size=None,
            ),
        ),
    ]
