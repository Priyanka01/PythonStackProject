# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-24 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=255)),
                ('t_created_at', models.DateTimeField(auto_now_add=True)),
                ('t_updated_at', models.DateTimeField(auto_now=True)),
                ('gl_guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='login_app.Guide')),
            ],
        ),
        migrations.CreateModel(
            name='GuideOffering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_date', models.CharField(max_length=255)),
                ('o_time', models.CharField(max_length=30)),
                ('o_location', models.CharField(max_length=255)),
                ('o_duration', models.CharField(max_length=255)),
                ('o_created_at', models.DateTimeField(auto_now_add=True)),
                ('o_updated_at', models.DateTimeField(auto_now=True)),
                ('o_guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offerings', to='login_app.Guide')),
            ],
        ),
        migrations.CreateModel(
            name='GuideSpeciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(max_length=255)),
                ('t_created_at', models.DateTimeField(auto_now_add=True)),
                ('t_updated_at', models.DateTimeField(auto_now=True)),
                ('gs_guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialitiies', to='login_app.Guide')),
            ],
        ),
        migrations.CreateModel(
            name='OfferingDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_day', models.CharField(max_length=20)),
                ('t_created_at', models.DateTimeField(auto_now_add=True)),
                ('t_updated_at', models.DateTimeField(auto_now=True)),
                ('o_guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offering_days', to='login_app.Guide')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_text', models.CharField(max_length=255)),
                ('r_rating', models.IntegerField()),
                ('r_created_at', models.DateTimeField(auto_now_add=True)),
                ('r_updated_at', models.DateTimeField(auto_now=True)),
                ('review_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_guides', to='login_app.Tourist')),
                ('reviewed_guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='login_app.Guide')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_location', models.CharField(max_length=255)),
                ('tour_datetime', models.DateTimeField()),
                ('tour_duration', models.DateTimeField()),
                ('t_created_at', models.DateTimeField(auto_now_add=True)),
                ('t_updated_at', models.DateTimeField(auto_now=True)),
                ('tour_booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_tours', to='login_app.Tourist')),
                ('tour_guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guided_tours', to='login_app.Guide')),
            ],
        ),
    ]
