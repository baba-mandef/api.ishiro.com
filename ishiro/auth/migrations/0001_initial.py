# Generated by Django 4.2 on 2024-02-13 22:09

from django.db import migrations, models
import ishiro.extra.tools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(db_index=True, default=ishiro.extra.tools.uuid_generator, unique=True)),
                ('key', models.CharField(max_length=40)),
                ('refresh', models.CharField(max_length=40, null=True)),
            ],
            options={
                'db_table': 'auth.auth_token',
                'managed': True,
            },
        ),
    ]
