# Generated by Django 2.2.5 on 2020-01-13 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_004',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('image', models.ImageField(upload_to='images')),
                ('url', models.URLField(max_length=250)),
            ],
        ),
    ]
