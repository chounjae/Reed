# Generated by Django 5.1.4 on 2025-01-27 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CUJO', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='unlike',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='postdash',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='postdash',
            name='unlike',
            field=models.IntegerField(default=0),
        ),
    ]
