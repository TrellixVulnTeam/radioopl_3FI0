# Generated by Django 3.0 on 2019-12-25 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrobbell', '0011_auto_20191225_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='img',
            field=models.ImageField(blank=True, height_field='height', upload_to='uploads/', width_field='width'),
        ),
    ]
