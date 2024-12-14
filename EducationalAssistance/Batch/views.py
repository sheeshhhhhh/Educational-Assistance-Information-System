from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, redirect, render
from EducationalAssistance.models import Batch, StatusChoices
from django.contrib.auth.decorators import login_required
from .forms import BatchForm

@login_required
def Batches(request):
    user = request.user
    batches = Batch.objects.filter(status=StatusChoices.Open, created_by=user).order_by('end_date')
    page = request.GET.get('page', 1)

    paginator = Paginator(batches, 10)
    try:
        batches = paginator.page(page)
    except PageNotAnInteger:
        batches = paginator.page(1)
    except EmptyPage:
        batches = paginator.page(paginator.num_pages)

    return render(request, 'batch/Batches.html', {'batches': batches })

@login_required
def BatchHistory(request):
    user = request.user
    if request.method == 'POST':
        batches = Batch.objects.filter(status=request.POST['status'], created_by=user)
    else:
        batches = Batch.objects.filter(status__in=[StatusChoices.Finished, StatusChoices.Cancelled], created_by=user)
    page = request.GET.get('page', 1)
    paginator = Paginator(batches, 10)

    try:
        batches = paginator.page(page)
    except PageNotAnInteger:
        batches = paginator.page(1)
    except EmptyPage:
        batches = paginator.page(paginator.num_pages)

    return render(request, 'batch/batchHistory.html', {'batches': batches })

@login_required
def BatchDetails(request, pk):
    batch = Batch.objects.prefetch_related('student_set').get(batch_id=pk)
    students = batch.student_set.all()

    if request.method == 'POST' and 'search_student' in request.POST:
        search_query = request.POST['search_student']
        students = students.filter(name__icontains=search_query)

    page = request.GET.get('page', 1)

    paginator = Paginator(students, 10)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(request, 'batch/batchDetails.html', {'batch': batch, 'students': students })

@login_required
def AddBatch(request):
    if request.method == 'POST':
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Batches)
    else:
        form = BatchForm()

    return render(request, 'batch/AddBatch.html', {'form': form})

@login_required
def UpdateBatch(request, pk):
    instance = Batch.objects.get(batch_id=pk)
    if request.method == 'POST':
        form = BatchForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(Batches)
    else:
        form = BatchForm(instance=instance)

    return render(request, 'batch/updateBatch.html', {'form': form})

@login_required
def CancelBatch(request, pk):
    batch = get_object_or_404(Batch, batch_id=pk)
    if not batch:
        return redirect(Batches)
    batch.status = StatusChoices.Cancelled
    batch.save()
    return redirect(Batches)