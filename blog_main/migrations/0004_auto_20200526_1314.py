# Generated by Django 3.0.6 on 2020-05-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_main', '0003_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image_link',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
