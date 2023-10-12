# Generated by Django 4.2.6 on 2023-10-12 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmodel',
            name='publication_date',
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='publication_year',
            field=models.IntegerField(default=1992, verbose_name='Дата публикации'),
            preserve_default=False,
        ),
    ]
