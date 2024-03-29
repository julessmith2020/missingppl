# Generated by Django 4.2.2 on 2023-06-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_missing', models.DateField()),
                ('age_at_missing', models.IntegerField(max_length=3)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2)),
                ('gender', models.CharField(max_length=1)),
                ('race', models.CharField(max_length=1)),
            ],
        ),
    ]
