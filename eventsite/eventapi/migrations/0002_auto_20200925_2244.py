# Generated by Django 3.1 on 2020-09-25 22:44

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eventapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 22, 44, 7, 908339, tzinfo=utc), verbose_name="Event's End Time"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 22, 44, 18, 612936, tzinfo=utc), verbose_name="Event's Start Time"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=255, verbose_name="Event's Location"),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=255, verbose_name="Event's name"),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name="Visitor's email address"),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_time', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapi.event')),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapi.visitor')),
            ],
            options={
                'unique_together': {('visitor', 'event')},
            },
        ),
        migrations.AddField(
            model_name='visitor',
            name='events',
            field=models.ManyToManyField(through='eventapi.Registration', to='eventapi.Event'),
        ),
    ]
