# Generated by Django 4.2 on 2024-02-20 13:23

from django.db import migrations, models
import django.db.models.deletion
import ishiro.extra.tools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('saver', '0003_alter_saver_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(db_index=True, default=ishiro.extra.tools.uuid_generator, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(max_length=150)),
                ('balance', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet_category', to='category.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saver.saver')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]