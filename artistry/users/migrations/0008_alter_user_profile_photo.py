# Generated by Django 4.2 on 2023-07-01 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_alter_user_profile_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_photo",
            field=models.ImageField(
                blank=True,
                default="media/profile/.trashed-1686832864-IMG_20230313_123948737.jpg",
                null=True,
                upload_to="profile/",
            ),
        ),
    ]
