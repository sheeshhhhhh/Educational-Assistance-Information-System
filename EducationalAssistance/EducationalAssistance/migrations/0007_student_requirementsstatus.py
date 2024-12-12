# Generated by Django 5.1.4 on 2024-12-12 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EducationalAssistance', '0006_alter_batch_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='requirementsStatus',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Completed', max_length=255),
        ),
    ]