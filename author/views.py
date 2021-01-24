from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from author.models import Author
from book.models import Book
from author.forms import AuthorForm


def author_listing_view(request):
    template_name = "author/author_listing.html"
    context = {}
    authors = Author.get_all()
    paginator = Paginator(authors, 10)
    page = request.GET.get('page', 1)
    try:
        context["authors"] = paginator.page(page)
    except PageNotAnInteger:
        context["authors"] = paginator.page(1)
    except EmptyPage:
        context["authors"] = paginator.page(paginator.num_pages)

    context["page"] = page
    context["page_title"] = "Authors"


    return render(request, template_name, context)


def author_detail_view(request, pk):
    template_name = "author/author_detail.html"
    author = Author.get_by_id(pk)
    books = list(Book.objects.filter(authors__id=pk))


    return render(request, template_name, {"books":books, "author":author})

def createAuthor(request):
    form = AuthorForm()
    context = {'form':form}
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            Author.create(request.POST['name'], request.POST['surname'], request.POST['patronymic'])
            return redirect("/authors")

    return render(request, 'author/author_form.html', context)



def updateAuthor(request, pk):
    author = Author.get_by_id(pk)
    form = AuthorForm(instance=author)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect("/authors")
    context = {'form': form}
    return render(request, 'author/author_form.html', context)

def deleteAuthor(request, pk):
    author = Author.get_by_id(pk)
    if request.method == 'POST':
        Author.delete_by_id(pk)
        return redirect('/authors')
    context = {'item': author}
    return render(request, 'author/delete.html', context)