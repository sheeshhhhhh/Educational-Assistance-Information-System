from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from EducationalAssistance.models import Batch, Student
from django.db.models import Q
from .forms import StudentForm


@login_required
def Students(request):
    user = request.user
    students = Student.objects.filter(batch__created_by=user).order_by('dateSubmitted')
    page = request.GET.get('page', 1)

    if request.method == 'POST':
        search = request.POST.get('search', '').strip()
        date_search = request.POST.get('date_search', '').strip()
        status = request.POST.get('status', '').strip()

        query = Q(batch__created_by=user)

        if search:
            query &= (Q(name__icontains=search) | Q(email__icontains=search) | Q(school__icontains=search) | Q(address__icontains=search))
        if date_search:
            print("being called")
            query &= Q(dateSubmitted=date_search)
        if status and status != "Choose a status":
            query &= Q(requirementsStatus=status)

        students = Student.objects.filter(query).order_by('dateSubmitted')

    paginator = Paginator(students, 10)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/Students.html', {'students': students })

@login_required
def StudentDetails(request, pk):
    student = Student.objects.get(student_id=pk)

    return render(request, 'students/studentDetails.html', {'student': student})

@login_required
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

@login_required
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

@login_required
def DeleteStudent(request, pk):
    student = get_object_or_404(Student, student_id=pk)

    # decrement the current count of the batch
    student.batch.current_count -= 1
    if not student.batch.is_full():
        student.batch.status = 'Open'
    
    student.batch.save()

    student.delete()
    return redirect('/batch/details/' + str(student.batch.batch_id))
    