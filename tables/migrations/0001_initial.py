# Generated by Django 3.2.13 on 2022-05-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('student_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('teacher_name', models.TextField()),
            ],
        ),
    ]
