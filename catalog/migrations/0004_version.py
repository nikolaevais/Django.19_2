# Generated by Django 5.0.7 on 2024-08-10 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_product_manufactured_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_version', models.BooleanField(default=True, verbose_name='Признак текущей версии')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]
