# Generated by Django 5.0 on 2024-02-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("poll", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="choice_trigger",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                verbose_name="Номер триггер вопроса",
            ),
        ),
    ]
