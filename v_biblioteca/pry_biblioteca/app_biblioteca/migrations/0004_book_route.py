# Generated by Django 4.2.7 on 2023-11-08 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_biblioteca', '0003_remove_author_age_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='route',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]