# Generated by Django 3.2.9 on 2021-12-05 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_tweet_is_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='is_liked',
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tweet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'tweet')},
            },
        ),
        migrations.AddField(
            model_name='tweet',
            name='liked_by',
            field=models.ManyToManyField(through='core.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]
