# Generated by Django 4.2.3 on 2023-08-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_merge_20230721_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_me',
            field=models.CharField(default=1, max_length=150, verbose_name='О себе'),
            preserve_default=False,
        ),
    ]
