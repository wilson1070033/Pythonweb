# Generated by Django 5.0.4 on 2024-04-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('Talk', models.CharField(max_length=1000)),
                ('joined_date', models.DateField(null=True)),
            ],
        ),
    ]