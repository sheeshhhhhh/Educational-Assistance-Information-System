# Generated by Django 5.1.4 on 2024-12-10 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EducationalAssistance', '0003_alter_batch_budget_alter_student_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Finished', 'Closed'), ('Cancelled', 'Cancelled')], default='Open', max_length=255),
        ),
    ]
