# Generated by Django 2.0.10 on 2019-02-26 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldetailsmodel',
            name='age',
        ),
    ]
