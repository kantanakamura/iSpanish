# Generated by Django 4.1 on 2023-05-23 12:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book_tutors', '0004_reviewoftutors_lecture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booktutors',
            old_name='date',
            new_name='end_datetime',
        ),
        migrations.RemoveField(
            model_name='booktutors',
            name='hour',
        ),
        migrations.AddField(
            model_name='booktutors',
            name='start_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
