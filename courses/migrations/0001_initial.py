# Generated by Django 3.0.7 on 2020-06-23 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField(auto_now=True)),
                ('end_date', models.DateTimeField(auto_now=True)),
                ('age_range', models.CharField(choices=[('1', '3-5 years'), ('2', '6-8 years'), ('3', '9-12 years'), ('4', '13-16 years')], max_length=1)),
                ('is_outdoors', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
