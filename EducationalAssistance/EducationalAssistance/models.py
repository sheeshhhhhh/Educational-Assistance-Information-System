from django.db import models
from django.contrib.auth.models import User

class StatusChoices(models.TextChoices):
    Open = 'Open'
    Finished = 'Finished'
    Cancelled = 'Cancelled'

class Batch(models.Model):
    batch_id = models.AutoField(primary_key=True)
    
    batch_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=255, choices=StatusChoices.choices, default=StatusChoices.Open)
    budget = models.IntegerField()

    limit = models.IntegerField()
    current_count = models.IntegerField(default=0)

    # Add foreign key to User
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="batches")

    def is_full(self):
        return self.current_count >= self.limit
    
    def __str__(self):
        return self.batch_name
    
    @property
    def formatted_start_date(self):
        return self.start_date.strftime('%m/%d/%Y')

class RequirementStatusCoices(models.TextChoices):
    Pending = 'Pending'
    Completed = 'Completed'

class Student(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=255)
    grade = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    requirementsStatus = models.CharField(max_length=255, choices=RequirementStatusCoices.choices, default=RequirementStatusCoices.Completed)
    
    dateSubmitted = models.DateField(auto_now_add=True)

    class Meta:
        constraints  = [
            models.UniqueConstraint(fields=['batch', 'email'], name="Unique email per Batch")
        ]

    def __str__(self):
        return self.name