# Generated by Django 3.0.7 on 2020-08-04 11:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Course Category',
                'verbose_name_plural': 'Course Categories',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Cid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Courses',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='OnlineCounsellingDetails',
            fields=[
                ('councelling_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='enter valid phone number', regex='^[6-9]\\d{9}$')])),
            ],
            options={
                'verbose_name': 'Free Councelling detail',
                'verbose_name_plural': 'Free Councelling details',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('subCat_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LandingPage.Category')),
            ],
            options={
                'verbose_name': 'Subcategories of Categories',
                'verbose_name_plural': 'Subcategories of Categories',
            },
        ),
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LandingPage.Course')),
            ],
            options={
                'verbose_name': 'Details about Courses and Facilitator',
                'verbose_name_plural': 'Details about Courses and Facilitators',
            },
        ),
    ]
