# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-05 19:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Season', models.CharField(max_length=10)),
                ('Year', models.IntegerField()),
                ('Name', models.CharField(max_length=20)),
                ('Percentage', models.FloatField()),
                ('Income', models.IntegerField()),
                ('Photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area', models.FloatField()),
                ('Income', models.IntegerField()),
                ('Village', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=6)),
                ('DoB', models.DateField()),
                ('Aadhar', models.CharField(max_length=12)),
                ('Number', models.CharField(max_length=10)),
                ('Income', models.IntegerField()),
                ('Photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Farmpoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seqno', models.IntegerField()),
                ('Lat', models.FloatField()),
                ('Lon', models.FloatField()),
                ('Farm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Farm')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lat', models.FloatField()),
                ('Lon', models.FloatField()),
                ('NoP', models.IntegerField()),
                ('F_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Farmer')),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=7)),
                ('DoB', models.DateField()),
                ('Aadhar', models.CharField(max_length=12)),
                ('Photo', models.FileField(upload_to='')),
                ('Relation', models.CharField(max_length=12)),
                ('Audio', models.FileField(upload_to='')),
                ('F_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Farmer')),
            ],
        ),
        migrations.CreateModel(
            name='PublicPlaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lat', models.FloatField()),
                ('Lon', models.FloatField()),
                ('Type', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=30)),
                ('Village', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Wells',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lat', models.FloatField()),
                ('Lon', models.FloatField()),
                ('Depth', models.FloatField()),
                ('Status', models.BooleanField()),
                ('AvgYield', models.FloatField()),
                ('Photo', models.FileField(upload_to='')),
                ('Farm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Farm')),
            ],
        ),
        migrations.AddField(
            model_name='farm',
            name='F_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Farmer'),
        ),
        migrations.AddField(
            model_name='crop',
            name='Farm_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Farm'),
        ),
    ]