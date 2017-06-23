# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-23 06:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=15)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('festival_name', models.CharField(max_length=30)),
                ('festival_website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='FestivalArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIbestival.Artist')),
                ('festival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIbestival.Festival')),
            ],
        ),
        migrations.CreateModel(
            name='FestivalGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('festival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIbestival.Festival')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='festivalgenre',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIbestival.Genre'),
        ),
        migrations.AddField(
            model_name='festival',
            name='artists',
            field=models.ManyToManyField(through='APIbestival.FestivalArtist', to='APIbestival.Artist'),
        ),
        migrations.AddField(
            model_name='festival',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIbestival.Date'),
        ),
        migrations.AddField(
            model_name='festival',
            name='genres',
            field=models.ManyToManyField(through='APIbestival.FestivalGenre', to='APIbestival.Genre'),
        ),
        migrations.AddField(
            model_name='festival',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIbestival.Location'),
        ),
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APIbestival.Genre'),
        ),
    ]
