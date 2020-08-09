# Generated by Django 3.0.7 on 2020-08-06 05:05

import LandingPage.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LandingPage', '0002_auto_20200804_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='days',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='months',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='VideoRecorded',
            fields=[
                ('Vid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('session_duration', models.DurationField()),
                ('video', models.FileField(blank=True, null=True, upload_to=LandingPage.models.content_Rfile_name)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LandingPage.Course')),
            ],
            options={
                'verbose_name': 'Recorded Sessions',
                'verbose_name_plural': 'Recorded Sessions',
            },
        ),
        migrations.CreateModel(
            name='LiveSession',
            fields=[
                ('Vid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('session_duration', models.DurationField()),
                ('session_start', models.TimeField(auto_now_add=True)),
                ('session_end', models.TimeField(auto_now_add=True)),
                ('video', models.FileField(blank=True, null=True, upload_to=LandingPage.models.content_file_name)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LandingPage.Course')),
            ],
            options={
                'verbose_name': 'Live Sessions',
                'verbose_name_plural': 'Live Sessions',
            },
        ),
    ]
