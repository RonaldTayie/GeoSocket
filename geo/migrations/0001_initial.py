# Generated by Django 4.0.5 on 2022-06-27 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(auto_created=True, default=uuid.uuid4, unique=True)),
                ('code', models.CharField(default='Decide Code', max_length=20, unique=True)),
                ('mac', models.CharField(max_length=30, unique=True)),
                ('package_name', models.CharField(default='Package Name', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GeoFence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(auto_created=True, default=uuid.uuid4, unique=True)),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StreamSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(auto_created=True, default=uuid.uuid4, unique=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='geo.device')),
                ('watchers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StreamMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_uid', models.UUIDField()),
                ('date_time', models.DateTimeField()),
                ('speed', models.CharField(blank=True, max_length=5, null=True)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='geo.streamsubscription')),
            ],
        ),
    ]
