# Generated by Django 3.0.8 on 2020-12-18 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CovidUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
                ('state_province', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('has_covid', models.BooleanField(default=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=15, default=0, max_digits=19, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=15, default=0, max_digits=19, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='search', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
