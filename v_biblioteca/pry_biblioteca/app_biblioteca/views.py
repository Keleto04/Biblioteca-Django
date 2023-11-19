from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Author


def home(request):
    # Renders the home page
    return render(request, 'index.html')


def list_authors(request):
    try:
        # Retrieves all authors from the database, ordered by primary key
        # pk can be replaced with id but you avoid name problems
        authors = Author.objects.all().order_by("pk")
        
        # Passes the authors to the 'authors.html' template
        return render(request, 'authors.html', {'authors': authors})

    except Exception as e:
        # Returns an error message if an exception occurs
        return HttpResponse(e)


def insert_author(request):
    try:
        if request.method == 'GET':
            # Renders the 'authors_form.html' template for a GET request
            return render(request, 'insert_author.html')
        else:
            # Creates a new Author instance with the provided name and surname in the POST request
            Author.objects.create(
                name=request.POST["name"],
                surname=request.POST["surname"])

            # Redirects to the '/authors/' URL after successful creation
            return redirect('/authors/')

    except Exception:
        return HttpResponse("No se pudo crear el autor")
    

def update_author(request, id):
    try:
        if request.method == "GET":
            # Retrieves all authors and a specific book based on the provided ID
            author = Author.objects.get(pk=id)
            
            # Renders the 'update_book.html' template with book and authors as context
            return render(request, "update_author.html", {"author": author})
        else:
            # Retrieves the book again and updates its attributes based on form data
            author = Author.objects.get(pk=id)
            
            # Sets the variables according to the data received in the POST request
            author_name = request.POST["name"]
            author_surname = request.POST["surname"]

            author.name = author_name
            author.surname = author_surname

            author.save()

            # Redirects to the '/books/' URL after successful update
            return redirect('/authors/')
    except Exception:
        # Returns an error message if an exception occurs
        return HttpResponse("No se pudo actualizar el autor")


def delete_author(request, id):
    try:
        # Retrieves a specific book based on the provided ID and deletes it
        author = Author.objects.get(pk=id)
        author.delete()
        # Redirects to the '/books/' URL after successful deletion
        return redirect('/authors/')
    except Exception:
        # Returns an error message if an exception occurs
        return HttpResponse("No se pudo eliminar el autor")


def list_books(request):
    try:
        # Retrieves all books from the database, ordered by the ID of their authors
        books = Book.objects.all().order_by("author__id")
        # Passes the books to the 'books.html' template
        return render(request, 'books.html', {'books': books})
    
    except Exception:
        return HttpResponse("No se pudieron listar los libros")


def insert_book(request):
    try:
        if request.method == 'GET':
            # Retrieves all authors and renders the 'insert_book.html' template with authors as context
            authors = Author.objects.all()
            return render(request, 'insert_book.html', {"authors": authors})
        else:
            # Handles form data from a POST request to create a new Book instance
            book_title = request.POST["title"]
            book_author_id = request.POST["author"]
            
            # Generates a route based on the presence of 'route' in the form data
            if request.POST["route"]: book_route = f'img/{request.POST["route"]}'

            else: book_route = f'img/{str(request.POST["title"]).lower().replace(' ', '_')}.jpg'
            
            # Retrieves the selected author and creates a new Book instance
            book_author = Author.objects.get(pk=book_author_id)
            Book.objects.create(
                title=book_title, author=book_author, route=book_route
            )
            # Redirects to the '/books/' URL after successful creation
            return redirect('/books/')
    except Exception:
        # Returns an error message if an exception occurs
        return HttpResponse("No se pudo crear el libro")



def update_book(request, id):
    try:
        if request.method == "GET":
            # Retrieves all authors and a specific book based on the provided ID
            authors = Author.objects.all().order_by("pk")
            book = Book.objects.get(pk=id)
            
            # Renders the 'update_book.html' template with book and authors as context
            return render(request, "update_book.html", {"book": book, "authors": authors})
        else:
            # Retrieves the book again and updates its attributes based on form data
            book = Book.objects.get(pk=id)
            
            # Sets the variables according to the data received in the POST request
            book_title = request.POST["title"]
            book_author_id = request.POST["author"]
            book_author = Author.objects.get(pk=book_author_id)
            book_route = request.POST["route"]

            book.title = book_title
            book.author = book_author
            book.route = book_route
            book.save()

            # Redirects to the '/books/' URL after successful update
            return redirect('/books/')
    except Exception:
        # Returns an error message if an exception occurs
        return HttpResponse("No se pudo actualizar el libro")


def delete_book(request, id):
    try:
        # Retrieves a specific book based on the provided ID and deletes it
        book = Book.objects.get(pk=id)
        book.delete()
        # Redirects to the '/books/' URL after successful deletion
        return redirect('/books/')
    except Exception:
        # Returns an error message if an exception occurs
        return HttpResponse("No se pudo eliminar el libro")
