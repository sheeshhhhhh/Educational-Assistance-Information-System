from django.shortcuts import redirect, render

from EducationalAssistance.models import Student

from .forms import StudentForm


# Create your views here.
def Students(request):

    return render(request, 'student/Students.html')

def StudentHistory(request):

    return render(request, 'student/studentHistory.html')

def StudentDetails(request, pk):
    student = Student.objects.get(student_id=pk)

    return render(request, 'student/studentDetails.html', {'student': student})

def AddStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Students)
    else:
        form = StudentForm()

    return render(request, 'student/addStudent.html', { 'form': form })

def UpdateStudent(request, pk):
    instance = Student.objects.get(student_id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(Students)
    else:
        form = StudentForm(instance=instance)
    
    return render(request, 'student/updateStudent.html', { 'form': form })

def DeleteStudent(request, pk):
    student = Student.objects.get(student_id=pk)
    if not student:
        return redirect(Students)
    student.delete()
    return redirect(Students)