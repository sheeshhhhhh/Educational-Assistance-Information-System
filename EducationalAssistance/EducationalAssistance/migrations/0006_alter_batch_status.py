# Generated by Django 5.1.4 on 2024-12-12 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EducationalAssistance', '0005_alter_batch_current_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Finished', 'Finished'), ('Cancelled', 'Cancelled')], default='Open', max_length=255),
        ),
    ]
