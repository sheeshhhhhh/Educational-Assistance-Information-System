# Generated by Django 5.1.4 on 2024-12-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('batch_id', models.AutoField(primary_key=True, serialize=False)),
                ('batch_name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(max_length=255)),
                ('Budget', models.IntegerField()),
                ('limit', models.IntegerField()),
                ('current_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=255)),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
    ]
