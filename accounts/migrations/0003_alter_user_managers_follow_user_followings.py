# Generated by Django 4.2.8 on 2024-12-29 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_profile_image_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_users', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('follower', 'following')},
            },
        ),
        migrations.AddField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(related_name='followers', through='accounts.Follow', to=settings.AUTH_USER_MODEL),
        ),
    ]
