# Generated by Django 3.0.7 on 2020-07-29 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('order_amount', models.BigIntegerField()),
                ('order_curruncy', models.CharField(blank=True, max_length=100, null=True)),
                ('order_status', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
