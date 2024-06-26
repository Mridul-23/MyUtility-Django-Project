from django.shortcuts import render, redirect, get_object_or_404
from .forms import NOTEForm
from .models import NOTES
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def notes(request):
    user = request.user
    form = NOTEForm()
    notes = NOTES.objects.filter(user=user)
    return render(request, "notes.html", context={"form": form, "notes": notes})


def add_note(request):
    if request.method == 'POST':
        form = NOTEForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  
            note.save() 
            return redirect('notes:notes')  
    else:
        form = NOTEForm()
    notes = NOTES.objects.filter(user=request.user)
    return render(request, 'notes.html', {'form': form, 'notes': notes})


def delete_note(request, id):
    note = get_object_or_404(NOTES, pk=id, user=request.user)
    note.delete()
    return redirect('notes:notes')