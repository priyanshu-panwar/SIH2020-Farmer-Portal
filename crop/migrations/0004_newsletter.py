# Generated by Django 2.2.6 on 2020-01-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0003_bid_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
