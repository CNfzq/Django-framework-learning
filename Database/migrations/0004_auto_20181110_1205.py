# Generated by Django 2.1.2 on 2018-11-10 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0003_ftest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ftest',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ftest',
            name='note',
            field=models.TextField(null=True),
        ),
    ]