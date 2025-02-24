# Generated by Django 3.0 on 2019-12-27 12:22

from django.db import migrations, models
from django.utils.text import slugify
# from ..models import Station


def slugify_title(apps, schema_editor):
    '''
    We can't import the Post model directly as it may be a newer
    version than this migration expects. We use the historical version.
    '''
    # station = apps.get_model('name', 'Station')
    Station = apps.get_model('Station', 'name')
    for post in Station.objects.all():
        post.slug = slugify(post.name)
        post.save()

class Migration(migrations.Migration):

    dependencies = [
        ('scrobbell', '0013_auto_20191225_2317'),
    ]

    operations = [
        migrations.RunPython(slugify_title),
    ]
