from django.shortcuts import render, redirect, get_object_or_404  
from django.shortcuts import render
from .models import Book
from .forms import BookForm
from django.urls import reverse
from django.contrib import messages


def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_detail.html', {'book': book})



def book_edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(reverse('books_collection'))
    else:
        form = BookForm(instance=book)

    page_title = f"Edit Book: {book.title}"  # set dynamic page title

    return render(request, 'books/book_edit.html', {'form': form, 'book': book, 'page_title': page_title})





def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        messages.error(request, 'Book deleted successfully!')
        return redirect('books_collection')  # Redirect to the list of booklists
    return render(request, 'books/book_delete.html', {'book': book})


def books_collection(request):
    books = Book.objects.all()
    return render(request, 'books/books_collection.html', {'books': books})



def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()

            # Get selected booklists IDs and update the booklists relationship
            selected_booklists = request.POST.getlist('booklists')
            book.booklists.set(selected_booklists)
            messages.success(request, 'Book added successfully!')

            return redirect('books_collection')
    else:
        form = BookForm()

    page_title = "Add new Book"  # set dynamic page title

    return render(request, 'books/book_edit.html', {'form': form,'page_title': page_title})
