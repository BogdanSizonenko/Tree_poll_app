# Generated by Django 5.0 on 2024-02-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("poll", "0003_rename_parent_question_question_parent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="choice",
            name="number_choice",
            field=models.CharField(
                max_length=20, verbose_name="Номер ответа по порядку"
            ),
        ),
    ]