# Generated by Django 4.0.3 on 2022-04-04 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_userprofile_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
    ]