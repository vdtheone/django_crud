# Generated by Django 4.2.6 on 2023-10-14 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0002_member_joined_date_member_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="joined_date",
            field=models.DateField(
                default=datetime.datetime(2023, 10, 15, 0, 1, 11, 532450)
            ),
        ),
    ]
