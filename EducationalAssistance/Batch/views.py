from django.shortcuts import render, redirect, get_object_or_404
from EducationalAssistance.models import Batch
from .forms import BatchForm

def Batches(request):
    batches = Batch.objects.all()

    return render(request, 'batch/Batches.html', {'batches': batches })

def BatchDetails(request, pk):
    batch = Batch.objects.get(batch_id=pk)

    return render(request, 'batch/BatchDetails.html', {'batch': batch})

def AddBatch(request):
    if(request.method == 'POST'):
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Batches)
    else:
        form = BatchForm()

    return render(request, 'batch/AddBatch.html', {'form': form})

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

def DeleteBatch(request, pk):
    batch = get_object_or_404(Batch, batch_id=pk)
    if not batch:
        return redirect(Batches)
    batch.delete()
    
    return redirect(Batches)