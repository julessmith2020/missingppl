# Generated by Django 4.2.2 on 2023-06-14 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webview', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age_at_missing',
            field=models.IntegerField(),
        ),
    ]
