# Generated by Django 3.1.6 on 2021-05-21 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storage', '0002_reviewaimodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='aimodel',
            name='uploaded_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='aimodel',
            name='uploader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
