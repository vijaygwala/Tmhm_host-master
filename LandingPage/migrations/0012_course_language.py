# Generated by Django 3.0.7 on 2020-08-31 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LandingPage', '0011_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.CharField(default='English', max_length=100),
            preserve_default=False,
        ),
    ]