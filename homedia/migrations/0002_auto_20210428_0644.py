# Generated by Django 3.2 on 2021-04-28 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homedia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='video_database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='DemoVideo',
            new_name='video_files',
        ),
        migrations.RenameField(
            model_name='video_files',
            old_name='video',
            new_name='vid',
        ),
    ]
