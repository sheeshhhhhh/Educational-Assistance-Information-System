from django.db import models

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

    def is_full(self):
        return self.current_count >= self.limit

class RequirementStatusCoices(models.TextChoices):
    Pending = 'Pending'
    Completed = 'Completed'

class Student(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=255)
    grade = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    requirementsStatus = models.CharField(max_length=255, choices=RequirementStatusCoices.choices, default=RequirementStatusCoices.Completed)