# Generated by Django 4.1 on 2024-02-09 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 9, 12, 13, 25, 446494, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
