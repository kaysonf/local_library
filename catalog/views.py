from django.shortcuts import render
from .models import (
            Book,
            BookInstance,
            Author,
            Genre,
)
from django.views import generic



# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count() # .all() is implied by default

    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors,
    }
    return render(request, 'catalog/index.html', context)

class BookListView(generic.ListView):
    model = Book
    template_name = 'catalog/book_list.html'
    context_object_name = 'book_list'
    paginate_by = 10
    def get_queryset(self):
        return Book.objects.all()[:5] # Get 5 books containing the title ho

    def get_context_data(self, **kwargs):
        # First get the existing context from our superclass.
        # Then add your new context information.
        # Then return the new (updated) context.

        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'
    context_object_name = 'book'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'catalog/author_detail.html'
    context_object_name = 'author'
