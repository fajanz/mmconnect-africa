# records/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Record
from .forms import RecordForm

def add_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_records')
    else:
        form = RecordForm()
    return render(request, 'records/add_record.html', {'form': form})

def view_records(request):
    records = Record.objects.all()
    return render(request, 'records/view_records.html', {'records': records})

def delete_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    if request.method == 'POST':
        record.delete()
        return redirect('view_records')
    return render(request, 'records/view_records.html')
