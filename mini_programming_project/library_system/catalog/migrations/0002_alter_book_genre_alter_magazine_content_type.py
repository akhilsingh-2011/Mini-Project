# Generated by Django 5.0.1 on 2024-01-29 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Genre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='Content_type',
            field=models.CharField(help_text='types of content featured (e.g., articles, interviews, reviews)', max_length=100),
        ),
    ]
