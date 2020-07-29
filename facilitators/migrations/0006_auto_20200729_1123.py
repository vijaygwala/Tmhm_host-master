# Generated by Django 3.0.7 on 2020-07-29 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilitators', '0005_facilitator'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilitator',
            name='Bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='facilitator',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='facilitator',
            name='profile',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='Mentor_profiles/'),
        ),
        migrations.AddField(
            model_name='facilitator',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='facilitator',
            name='zipcode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
