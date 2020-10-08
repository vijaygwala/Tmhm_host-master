import LandingPage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LandingPage', '0011_partners'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=LandingPage.models.video_course_path),
        ),
        migrations.AddField(
            model_name='coursevideo',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=LandingPage.models.video_path),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(blank=True, default=2000, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default/course_thumbnail.png', null=True, upload_to='courses/'),
        ),
    ]