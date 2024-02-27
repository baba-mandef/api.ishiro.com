# Generated by Django 4.2 on 2024-02-20 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wallet', '0001_initial'),
        ('transfer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='receiver_wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_wallet', to='wallet.wallet'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='wallet_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet_source', to='wallet.wallet'),
        ),
    ]
