from django.shortcuts import render
from django.shortcuts import get_object_or_404
from store.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import random
from django.db.models import Avg

# Create your views here.

def index(request):
    return render(request, 'store/index.html')

def bookDetailView(request, bid):
    template_name = 'store/book_detail.html'
    context = {
        'book': None, # set this to an instance of the required book
        'num_available': None, # set this to the number of copies of the book available, or 0 if the book isn't available
    }
    # START YOUR CODE HERE
    book_needed=Book.objects.get(id=bid)
    context['book']=book_needed
    context['num_available']=BookCopy.objects.filter(book=book_needed).filter(status=False).count()
    
    return render(request, template_name, context=context)


@csrf_exempt
def bookListView(request):
    template_name = 'store/book_list.html'
    context = {
        'books': None, # set this to the list of required books upon filtering using the GET parameters
                       # (i.e. the book search feature will also be implemented in this view)
    }
    get_data = request.GET
    print(get_data)
    if not bool(get_data):
    # START YOUR CODE HERE
        context['books']=Book.objects.all()
    else:
        title=get_data['title']
        if title != '':
            books=Book.objects.filter(title__icontains=title)
        author=get_data['author']
        if author != '':
            books=books | Book.objects.filter(author__icontains=author)
        genre=get_data['genre']
        if genre != '':
            books=books | Book.objects.filter(genre__icontains=genre)
        print(title,author,genre)
        context['books']=books
        return render(request, template_name, context=context)
    print(context)
    
    return render(request, template_name, context=context)



@login_required
def viewLoanedBooks(request):
    template_name = 'store/loaned_books.html'
    context = {
        'books': None,
    }
    '''
    The above key 'books' in the context dictionary should contain a list of instances of the 
    BookCopy model. Only those book copies should be included which have been loaned by the user.
    '''
    # START YOUR CODE HERE
    context['books']=BookCopy.objects.filter(borrower=request.user)
    


    return render(request, template_name, context=context)

@csrf_exempt
@login_required
def loanBookView(request):
    response_data = {
        'message': None,
    }
    '''
    Check if an instance of the asked book is available.
    If yes, then set the message to 'success', otherwise 'failure'
    '''
    # START YOUR CODE HERE
    print(request.POST['bid'])
    book_id = request.POST['bid'] # get the book id from post data
    book_needed=Book.objects.get(id=book_id)
    copy=BookCopy.objects.filter(book=book_needed).filter(status=False)
    copylist=list(copy)
    print(copylist)
    num=copy.count()
    print(num)
    if(num==0):
        response_data['message']='failure'
    else:
        response_data['message']='success'
        loaned=copy[0]
        print(loaned, timezone.now())
        loaned.status=True
        loaned.borrow_date=timezone.now()
        loaned.borrower=request.user
        loaned.save()
        #print(loaned.status)

    print(response_data['message'])
    print(request.user)
    


    return JsonResponse(response_data)

'''
FILL IN THE BELOW VIEW BY YOURSELF.
This view will return the issued book.
You need to accept the book id as argument from a post request.
You additionally need to complete the returnBook function in the loaned_books.html file
to make this feature complete
''' 
@csrf_exempt
@login_required
def returnBookView(request):
    response_data = {
        'message': None,
    }
    print(request.POST['bid'])
    book_id = request.POST['bid'] # get the book id from post data
    #book_needed=Book.objects.get(id=book_id)
    copy=BookCopy.objects.filter(id=book_id)
    #num=copy.count()
    #print(num)
    response_data['message']='success'
    loaned=copy[0]
    #print(loaned, timezone.now())
    loaned.status=False
    loaned.borrow_date=None
    loaned.borrower=None
    loaned.save()
    #print(loaned.status)

    print(response_data['message'])
    print(request.user)
    return JsonResponse(response_data)

@csrf_exempt
@login_required
def ratingView(request):
    response_data = {
        'message': None,
    }
    if request.method == 'POST':
        book_id = Book.objects.get(id=request.POST['bid'])
        num = Bookrating.objects.filter(book=book_id).filter(reader=request.user).count()
        if num==0:
            create = Bookrating(book=book_id, reader=request.user, rating=request.POST['rating'])
            create.save()
            response_data['message']='Successfully rated'
        else:
            ratechanger = Bookrating.objects.filter(book=book_id).filter(reader=request.user)
            book = ratechanger[0]
            book.rating = request.POST['rating']
            book.save()
            print(book.rating)
            response_data['message']='Rating Updated'
        print("rated:",request.POST['rating'])
        rates=Bookrating.objects.filter(book=book_id)
        average = rates.aggregate(Avg('rating'))
        book_id.rating = average['rating__avg']
        book_id.save()
        print(average['rating__avg'])
    
    return JsonResponse(response_data)