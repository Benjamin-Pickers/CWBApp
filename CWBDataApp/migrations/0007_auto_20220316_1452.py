# Generated by Django 2.1 on 2022-03-16 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CWBDataApp', '0006_picsum'),
    ]

    operations = [
        migrations.AddField(
            model_name='picsum',
            name='supervisor',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='picsum',
            name='temp1',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='picsum',
            name='temp2',
            field=models.BooleanField(),
        ),
    ]
