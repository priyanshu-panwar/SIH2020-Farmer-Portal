# Generated by Django 2.2.6 on 2020-01-07 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics')),
                ('contact', models.CharField(blank=True, max_length=13, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('accNo', models.CharField(max_length=20)),
                ('ifscNo', models.CharField(max_length=20)),
                ('bankName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Bank')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
