# Generated by Django 2.0.7 on 2018-07-04 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffuser',
            name='phonenum',
            field=models.CharField(max_length=14),
        ),
    ]
