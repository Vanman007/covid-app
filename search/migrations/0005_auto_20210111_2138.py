# Generated by Django 3.0.8 on 2021-01-11 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_coviduser_covid_risk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('covid_info', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(blank=True, decimal_places=15, default=0, max_digits=19, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=15, default=0, max_digits=19, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='coviduser',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='coviduser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='coviduser',
            name='covid_risk',
        ),
        migrations.RemoveField(
            model_name='coviduser',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='coviduser',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='coviduser',
            name='state_province',
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('covid_info', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(blank=True, decimal_places=15, default=0, max_digits=19, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=15, default=0, max_digits=19, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Country')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='coviduser',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.City'),
        ),
        migrations.AlterField(
            model_name='coviduser',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Country'),
        ),
    ]
