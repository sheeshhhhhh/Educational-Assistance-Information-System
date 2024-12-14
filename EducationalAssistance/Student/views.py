from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from EducationalAssistance.models import Batch, Student
from .forms import StudentForm


# use for managing student but not adding
def Students(request):
    students = Student.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(students, 10)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/Students.html', {'students': students })

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

            # increment the current count of the batch
            batch_instance.current_count += 1
            # if the batch is full, set the status to Finished
            if batch_instance.is_full():
                batch_instance.status = 'Finished'
                
            batch_instance.save()

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

    # decrement the current count of the batch
    student.batch.current_count -= 1
    if not student.batch.is_full():
        student.batch.status = 'Open'
    
    student.batch.save()

    student.delete()
    return redirect('/batch/details/' + str(student.batch.batch_id))
    