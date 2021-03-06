# Generated by Django 3.2 on 2021-08-11 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homedia', '0007_alter_files_file_up'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(upload_to='media')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upload_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
