# Generated by Django 3.1.4 on 2021-01-01 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='party_number',
            field=models.IntegerField(default=0),
        ),
    ]
