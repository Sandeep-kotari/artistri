# Generated by Django 4.2 on 2023-07-01 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0010_alter_user_profile_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_photo",
            field=models.ImageField(
                default="/static/images/default.jpg", upload_to="profile/"
            ),
        ),
    ]
