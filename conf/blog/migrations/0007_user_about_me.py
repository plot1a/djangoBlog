# Generated by Django 4.2.3 on 2023-07-28 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_user_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_me',
            field=models.CharField(default=1, max_length=150, verbose_name='О себе'),
            preserve_default=False,
        ),
    ]
