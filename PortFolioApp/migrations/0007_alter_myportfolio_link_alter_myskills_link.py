# Generated by Django 5.0.1 on 2024-02-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortFolioApp', '0006_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myportfolio',
            name='link',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='myskills',
            name='link',
            field=models.TextField(max_length=150),
        ),
    ]
