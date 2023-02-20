# Generated by Django 4.1.7 on 2023-02-20 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='listing',
            name='shoe',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='shoeSize',
            field=models.CharField(max_length=10),
        ),
    ]