# Generated by Django 3.2.7 on 2022-04-09 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default=1, upload_to='profile_image/'),
            preserve_default=False,
        ),
    ]
