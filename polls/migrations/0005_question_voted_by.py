# Generated by Django 4.1.3 on 2022-12-04 09:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_question_description_question_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='voted_by',
            field=models.ManyToManyField(related_name='voted_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
