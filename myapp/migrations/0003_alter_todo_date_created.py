# Generated by Django 5.1.1 on 2024-09-27 07:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_alter_todo_detail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="date_created",
            field=models.DateTimeField(auto_now=True),
        ),
    ]