# Generated by Django 3.1.2 on 2020-10-24 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0003_auto_20201024_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='issue_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]