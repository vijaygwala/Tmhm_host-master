from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LandingPage', '0010_course_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('Cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LandingPage.Course')),
            ],
            options={
                'verbose_name': 'Corporates',
                'verbose_name_plural': 'Corporates',
            },
        ),
    ]