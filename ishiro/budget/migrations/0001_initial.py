# Generated by Django 4.2 on 2024-02-25 11:28

from django.db import migrations, models
import django.db.models.deletion
import ishiro.extra.tools


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('saver', '0003_alter_saver_currency'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(db_index=True, default=ishiro.extra.tools.uuid_generator, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('limit', models.IntegerField()),
                ('spent', models.IntegerField()),
                ('remaining', models.IntegerField()),
                ('period', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budget_category', to='category.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saver.saver')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
