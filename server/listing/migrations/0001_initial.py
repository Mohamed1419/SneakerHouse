# Generated by Django 4.1.7 on 2023-02-17 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoe', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('shoeSize', models.CharField(max_length=200)),
            ],
        ),
    ]