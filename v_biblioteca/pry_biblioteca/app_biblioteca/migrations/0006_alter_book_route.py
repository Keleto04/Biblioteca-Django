# Generated by Django 4.2.7 on 2023-11-13 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_biblioteca', '0005_alter_book_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='route',
            field=models.CharField(blank=True, default='<django.db.models.fields.charfield> +"jpg"', max_length=100, null=True),
        ),
    ]
