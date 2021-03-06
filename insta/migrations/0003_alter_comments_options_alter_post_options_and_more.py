# Generated by Django 4.0.3 on 2022-04-07 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_rename_userprofile_post_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_posted']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='insta.post'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.TextField(max_length=150),
        ),
    ]
