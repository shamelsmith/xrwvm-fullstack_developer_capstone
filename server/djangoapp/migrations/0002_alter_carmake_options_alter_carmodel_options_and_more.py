# Generated by Django 5.1.1 on 2024-09-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carmake',
            options={},
        ),
        migrations.AlterModelOptions(
            name='carmodel',
            options={},
        ),
        migrations.AddField(
            model_name='carmake',
            name='create_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='create_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterModelTable(
            name='carmake',
            table=None,
        ),
        migrations.AlterModelTable(
            name='carmodel',
            table=None,
        ),
    ]
