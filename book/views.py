from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from author.models import Author
from book.models import Book
from book.forms import BookForm


def book_listing_view(request):
    template_name = "books_listing.html"
    context = {}
    books = Book.get_all()
    paginator = Paginator(books, 10)
    page = request.GET.get('page', 1)
    try:
        context["books"] = paginator.page(page)
    except PageNotAnInteger:
        context["books"] = paginator.page(1)
    except EmptyPage:
        context["books"] = paginator.page(paginator.num_pages)

    context["page_title"] = "Books in stock"
    context["page"] = page

    return render(request, template_name, context)


def book_detail_view(request, pk):
    template_name = "book_detail.html"
    book = Book.get_by_id(pk)

    return render(request, template_name, {"book":book, "page_title":book.name})

########### SPRINT 17 ############

def createBook(request):
    form = BookForm()
    context = {'form':form}
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Book.create(request.POST['name'], request.POST['description'], request.POST['count'], request.POST['authors'])
            return redirect("/books")

    return render(request, 'book_form.html', context)



def updateBook(request, pk):
    book = Book.get_by_id(pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("/books")
    context = {'form': form}
    return render(request, 'book_form.html', context)

def deleteBook(request, pk):
    book = Book.get_by_id(pk)
    if request.method == 'POST':
        Book.delete_by_id(pk)
        return redirect('/books')
    context = {'item': book}
    return render(request, 'book_delete.html', context)