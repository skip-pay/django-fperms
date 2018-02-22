# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-22 16:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Perm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('codename', models.CharField(max_length=100, verbose_name='codename')),
            ],
            options={
                'verbose_name': 'Permission',
                'verbose_name_plural': 'Permissions',
                'manager_inheritance_from_future': True,
            },
        ),
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FieldPerm',
            fields=[
                ('perm_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_perms.Perm')),
                ('field_name', models.CharField(max_length=100, verbose_name='field name')),
            ],
            options={
                'verbose_name': 'Field Permission',
                'verbose_name_plural': 'Field Permissions',
                'manager_inheritance_from_future': True,
            },
            bases=('django_perms.perm',),
        ),
        migrations.CreateModel(
            name='GlobalPerm',
            fields=[
                ('perm_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_perms.Perm')),
            ],
            options={
                'verbose_name': 'Global Permission',
                'verbose_name_plural': 'Global Permissions',
                'manager_inheritance_from_future': True,
            },
            bases=('django_perms.perm',),
        ),
        migrations.CreateModel(
            name='ObjectPerm',
            fields=[
                ('perm_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_perms.Perm')),
                ('object_pk', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Object Permission',
                'verbose_name_plural': 'Object Permissions',
                'manager_inheritance_from_future': True,
            },
            bases=('django_perms.perm',),
        ),
        migrations.AddField(
            model_name='userpermission',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_perms.Perm'),
        ),
        migrations.AddField(
            model_name='userpermission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='perm',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='content type'),
        ),
        migrations.AddField(
            model_name='perm',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_django_perms.perm_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='grouppermission',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_perms.Perm'),
        ),
    ]
