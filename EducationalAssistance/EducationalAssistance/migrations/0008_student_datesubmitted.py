# Generated by Django 5.1.4 on 2024-12-12 11:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EducationalAssistance', '0007_student_requirementsstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dateSubmitted',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
