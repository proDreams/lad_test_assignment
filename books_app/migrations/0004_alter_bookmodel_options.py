# Generated by Django 4.2.6 on 2023-10-13 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0003_commentmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmodel',
            options={'ordering': ['title'], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
