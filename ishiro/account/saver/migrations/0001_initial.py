# Generated by Django 4.2 on 2024-02-13 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ishiro_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saver',
            fields=[
                ('avatar', models.ImageField(null=True, upload_to='avatar/')),
                ('activated', models.DateTimeField(null=True)),
                ('deactivated', models.DateTimeField(null=True)),
                ('verified', models.DateTimeField(null=True)),
                ('verification_code', models.CharField(max_length=6)),
                ('deactivated_reason', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('currency', models.CharField(max_length=10)),
            ],
            options={
                'managed': True,
            },
            bases=('ishiro_user.user', models.Model),
        ),
    ]
