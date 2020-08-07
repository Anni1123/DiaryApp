from django.shortcuts import render,redirect
from .models import Entry
# Create your views here.

from .forms import EntryForm
def index(request):
    entries = Entry.objects.order_by('-date_posted')
    context = {'entries': entries}
    return render(request,'entries/index.html',context)

def add(request):
    if request.method == 'POST':
        forms = EntryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    else:
        forms=EntryForm()
    context={'forms':forms}
    return render(request,'entries/add.html',context)