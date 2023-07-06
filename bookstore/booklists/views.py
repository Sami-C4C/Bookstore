from .models import Booklist
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BooklistForm
from django.urls import reverse
from django.contrib import messages



def booklist(request, booklist_id):
    booklist = Booklist.objects.get(pk=booklist_id)
    return render(request, 'booklist.html', {'booklist': booklist})


def booklist_edit(request, booklist_id):
    booklist = get_object_or_404(Booklist, pk=booklist_id)
    if request.method == 'POST':
        form = BooklistForm(request.POST, instance=booklist)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booklist edited successfully!')
            return redirect(reverse('booklists_collection'))
    else:
        form = BooklistForm(instance=booklist)


    page_title = f"Edit Booklist: {booklist.title}"  # set dynamic page title

    return render(request, 'booklists/booklist_edit.html', {'form': form, 'booklist': booklist, 'page_title': page_title})





def booklist_delete(request, booklist_id):
    booklist = get_object_or_404(Booklist, pk=booklist_id)
    if request.method == 'POST':
        booklist.delete()
        messages.error(request, 'Booklist deleted successfully!')
        return redirect('booklists_collection')  # Redirect to the list of booklists
    return render(request, 'booklists/booklist_delete.html', {'booklist': booklist})


def booklists_collection(request):
    booklists = Booklist.objects.all()
    return render(request, 'booklists/booklists_collection.html', {'booklists': booklists})



def booklist_new(request):
    if request.method == 'POST':
        form = BooklistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booklist added successfully!')
            return redirect('booklists_collection')
    else:
        form = BooklistForm()

    page_title = 'Add New Booklist'
    return render(request, 'booklists/booklist_edit.html', {'form': form, 'page_title': page_title})


