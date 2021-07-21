# Library Management System

## Introduction

In this project, I will be working on the Django backend of a library web application.



### Setting up the project

- Make sure `python3.7` and `pip` are installed. Install `pipenv` by running `pip install pipenv`.
- Install python dependencies using the command `pipenv install` Please use only pipenv for managing dependencies (Follow this [link](https://realpython.com/pipenv-guide/) if you are new to pipenv).
- To activate this project's virtualenv, run `pipenv shell`.
- Run `python manage.py migrate` to apply migrations.
- Start the development server using `python manage.py runserver`

### Working
* There will be several books present in the Library, which can be added or removed only from the backend (Book model).
* Every book will have several instances. Again, this can be added or removed only from the backend. Note that each instance denotes a physical copy of the book (BookCopy model).
* As an example, if a book B1 has 5 copies, then there shall be 5 BookCopy instances corresponding to the book B1.
* While borrowing a book, a logged in user can borrow any instance of the BookCopy model whose status is available. A user is allowed to borrow multiple copies of the same book. After successfully borrowing a copy, the number of copies of the book available in the library will decrease. That is, if the user borrows the book B1, then the number of instances of book B1 will become 4. The instance won't get deleted on borrowing as it represents a physical copy of the book.
* A user can return a copy of the book, and thereby, the number of copies of the book available will increase by 1, for each book copy returned.
* The library system would also allow the user to rate a particular book, which will be used to calculate the average rating of the book. The ratings will be given to a book, and not to the copy of a book. Also, a user can rate a book multiple times, and in that case, only the last rating given by the user to the book will persist.


## Tasks
#### Stage 1
Only a logged in user can view the loaned books or issue a book.

* Book Detail View - Shows the details of a book like no. of copies available, its rating given by users, its genre and author.
* Book List View - Shows the list of all the books that are available
* View Loaned Books - Shows the books which are loaned by an authorized user
* Issue a Book - Implements the function of issuing a book

#### Stage 2
* We create a view that will accept Book Copy ID as an argument and mark the appropriate Book Copy as returned and return an appropriate response.
* We additionally write the JavaScript code to make a POST request to your view and display an appropriate message to the user after the response arrives.

#### Stage 3
In this stage, I implement a rating system.
* The system allows the user to enter any integer between 0 to 10 (both inclusive) and the final rating would be the average of all the user ratings given to the book and should be a real number.
* The ratings would be given to a Book issued by a user, and not a Book Copy.
* The ratings must be modifiable. Also, if a user has rated a book multiple times, then only the last rating given by the user should matter, any previous ratings should not contribute to the average rating of the book.
* As an example, if there are two users U1 and U2, and they have rated a book as 8 and 10, respectively, then the average rating would be 9.0. If the user U1 later changes the rating to 9, then the average rating of the book should become 9.5.
* Only a logged in user should be allowed to rate a book, but others may view the average rating of the book.
* We add an integer field with a submit button in the Book Detail template.

#### Stage 4
In the authentication app, views for login, logout and user registration are created. I created basic frontend templates for these views.


