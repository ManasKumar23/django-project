# Generated by Django 4.0.3 on 2022-04-01 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=250)),
                ('description', models.CharField(blank=True, max_length=250)),
            ],
        ),
    ]
