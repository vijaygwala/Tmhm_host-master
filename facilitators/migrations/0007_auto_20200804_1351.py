# Generated by Django 3.0.7 on 2020-08-04 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facilitators', '0006_auto_20200729_1123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name': 'Experience Detail', 'verbose_name_plural': 'Experience Details'},
        ),
        migrations.AlterModelOptions(
            name='facilitator',
            options={'verbose_name': 'Approved Facilitator', 'verbose_name_plural': 'Approved Facilitators'},
        ),
        migrations.AlterModelOptions(
            name='facilitatorqueries',
            options={'verbose_name': 'Queries by Facilitator', 'verbose_name_plural': 'Queries by Facilitators'},
        ),
    ]