# Generated by Django 2.1 on 2022-03-23 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CWBDataApp', '0007_auto_20220316_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='cisEmailSubject',
            fields=[
                ('subject', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
