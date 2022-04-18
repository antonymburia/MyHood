# Generated by Django 4.0.3 on 2022-04-18 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0002_business_hood_delete_category_post_business_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='link',
        ),
        migrations.AddField(
            model_name='business',
            name='contact',
            field=models.TextField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='hood',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
