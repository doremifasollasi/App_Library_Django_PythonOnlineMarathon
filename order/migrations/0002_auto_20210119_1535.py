# Generated by Django 3.1.5 on 2021-01-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='plated_end_at',
            field=models.DateTimeField(verbose_name='Returning Date'),
        ),
    ]