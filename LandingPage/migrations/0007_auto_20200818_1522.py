# Generated by Django 3.0.7 on 2020-08-18 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LandingPage', '0006_auto_20200816_1329'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VideoRecorded',
            new_name='CourseVideo',
        ),
        migrations.AlterModelOptions(
            name='coursevideo',
            options={},
        ),
    ]
