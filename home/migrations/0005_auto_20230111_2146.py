# Generated by Django 3.1.3 on 2023-01-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20230111_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='ph',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
