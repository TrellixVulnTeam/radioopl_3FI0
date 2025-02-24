# Generated by Django 3.0 on 2019-12-12 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrobbell', '0002_histlast'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=150)),
                ('artist', models.ManyToManyField(to='scrobbell.Artist')),
                ('feat', models.ManyToManyField(related_name='feat', to='scrobbell.Artist')),
            ],
        ),
    ]
