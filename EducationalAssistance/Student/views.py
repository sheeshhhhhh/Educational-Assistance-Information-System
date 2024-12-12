from django.shortcuts import get_object_or_404, redirect, render

from EducationalAssistance.models import Batch, Student

from .forms import StudentForm


# use for managing student but not adding
def Students(request):
    students = Student.objects.all()

    return render(request, 'students/Students.html', {'students': students})

# use for managing student in the batch and also adding
# not being used
def StudentsInBatch(request, pk):
    students = Student.objects.filter(batch_id=pk)

    return render(request, 'students/Students.html', {'students': students})

# when user click this it will show the details of the student
def StudentDetails(request, pk):
    student = Student.objects.get(student_id=pk)

    return render(request, 'students/studentDetails.html', {'student': student})

def AddStudent(request, batch_id):
    batch_instance = get_object_or_404(Batch, batch_id=batch_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.batch = batch_instance
            student.save()
            return redirect('/batch/details/' + str(batch_id))
    else:
        form = StudentForm()

    return render(request, 'students/addStudent.html', { 'form': form, 'batch': batch_instance })

def UpdateStudent(request, pk):
    instance = Student.objects.get(student_id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/batch/details/' + str(instance.batch.batch_id))
    else:
        form = StudentForm(instance=instance)
    
    return render(request, 'students/updateStudent.html', { 'form': form })

def DeleteStudent(request, pk):
    student = get_object_or_404(Student, student_id=pk)

    student.delete()
    return redirect('/batch/details/' + str(student.batch.batch_id))
    