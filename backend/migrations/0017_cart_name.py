# Generated by Django 3.0.8 on 2020-07-18 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_auto_20200718_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
