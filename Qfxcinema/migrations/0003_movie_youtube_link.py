# Generated by Django 2.0 on 2017-12-21 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Qfxcinema', '0002_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='youtube_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]