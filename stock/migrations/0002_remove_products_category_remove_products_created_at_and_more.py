# Generated by Django 5.2 on 2025-04-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.RemoveField(
            model_name='products',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]
