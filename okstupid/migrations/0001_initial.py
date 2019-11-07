# Generated by Django 2.2.7 on 2019-11-07 00:36

from django.conf import settings
import django.core.files.storage
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2)])),
                ('gender', models.CharField(blank=True, max_length=5)),
                ('age', models.PositiveIntegerField()),
                ('height', models.CharField(max_length=5)),
                ('location', models.CharField(max_length=25)),
                ('job_title', models.CharField(max_length=25)),
                ('education', models.CharField(max_length=50)),
                ('hometown', models.CharField(max_length=25)),
                ('drinker', models.BooleanField(default=False)),
                ('smoker', models.BooleanField(default=False)),
                ('photo_one', models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to='')),
                ('photo_two', models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to='')),
                ('photo_three', models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to='')),
                ('prompt_one', models.CharField(max_length=255)),
                ('prompt_two', models.CharField(max_length=255)),
                ('prompt_three', models.CharField(max_length=255)),
                ('age_preference_max', models.PositiveIntegerField()),
                ('age_preference_min', models.PositiveIntegerField()),
                ('gender_preference', models.CharField(blank=True, max_length=25)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Matched',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed', models.BooleanField(default=False)),
                ('profile_id_connect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to=settings.AUTH_USER_MODEL)),
                ('profile_id_init', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
