# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-11 23:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('generic', 'generic'), ('model', 'model'), ('object', 'object'), ('field', 'field')], default='generic', max_length=10)),
                ('codename', models.CharField(max_length=100, verbose_name='codename')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('object_id', models.SmallIntegerField(blank=True, null=True, verbose_name='object pk')),
                ('field_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='field name')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='content type')),
                ('groups', models.ManyToManyField(related_name='perms', to='auth.Group')),
                ('users', models.ManyToManyField(related_name='perms', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'permission',
                'verbose_name_plural': 'permissions',
                'ordering': ('content_type', 'object_id', 'field_name', 'codename'),
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='perm',
            unique_together=set([('type', 'codename', 'content_type', 'object_id', 'field_name')]),
        ),
    ]
