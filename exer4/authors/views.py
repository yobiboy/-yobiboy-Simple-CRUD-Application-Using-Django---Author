from django.shortcuts import redirect, render
from .models import *
from .forms import *

def home(request):
    authors = Authors.objects.all()
    books = Books.objects.all()
    data = {"authors": authors, "books": books}
    # books = Books.objects.all()
    # data2 = {"books": books}
    return render(request, "authors/home.html", data)

def createAuthor(request):
    form = AuthorForm()
    if(request.method == "POST"):
        form = AuthorForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect("/")
    data = {"form": form}
    return render(request, "authors/createAuthor.html", data)
    
def updateAuthor(request, pk):
    author = Authors.objects.get(id=pk)
    form = AuthorForm(instance=author)

    if(request.method == "POST"):
        form = AuthorForm(request.POST, instance=author)
        if(form.is_valid):
            form.save()
            return redirect("/")

    data = {"form": form}
    return render(request, "authors/updateAuthor.html", data)

def deleteAuthor(request, pk):
    author = Authors.objects.get(id=pk)
    author.delete()
    return redirect("/")



def home1(request):
    books = Books.objects.all()
    data = {"books": books}
    return render(request, "authors/home.html", data)

def createBook(request):
    form = BookForm()
    if(request.method == "POST"):
        form = BookForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect("/")
    data = {"form": form}
    return render(request, "authors/createBook.html", data)
    
def updateBook(request, pk):
    book = Books.objects.get(id=pk)
    form = BookForm(instance=book)

    if(request.method == "POST"):
        form = BookForm(request.POST, instance=book)
        if(form.is_valid):
            form.save()
            return redirect("/")

    data = {"form": form}
    return render(request, "authors/updateBook.html", data)

def deleteBook(request, pk):
    book = Books.objects.get(id=pk)
    book.delete()
    return redirect("/")