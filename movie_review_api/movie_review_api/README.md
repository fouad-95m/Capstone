# Movie Review API

This is a Django-based REST API for managing movie reviews. Users can create, read, update, and delete movie reviews. The API is protected with user authentication and supports role-based access.

## Features
- CRUD operations for movie reviews.
- User authentication (signup, login, logout).
- List and detail views for movies and reviews.
- Review filtering by movie.
- Role-based access control.

## Installation

### Prerequisites
- Python 3.8+ (use \python3 --version\ to check)
- Django 3.0+ (use \pip show django\ to check)
- Django Rest Framework
- Django Filters

### Setup Instructions

1. **Clone the repository**:

\\\ash
git clone https://github.com/Capstone/movie-review-api.git
cd movie-review-api
\\\" >> README.md
echo " >> README.md
echo 
3.
**Install
dependencies**: >> README.md
echo " >> README.md
echo \\\ash >> README.md
echo pip
install
-r
requirements.txt >> README.md
echo \\\"

4. **Apply migrations**:

\\\ash
python manage.py migrate

6. **Run the development server**:

\\\ash
python manage.py runserver
\\\" >> README.md
echo " >> README.md
echo 
The
server
will
be
running
at
\http://127.0.0.1:8000/\. >> README.md
echo " >> README.md
echo 7.
**Access
the
API**: >> README.md
echo -
Movies:
\/api/movies/\"
- Reviews: \/api/reviews/\" >> README.md
echo 
-
Signup:
\/signup/\"
You can test the API using tools like Postman or Curl.

- To create a review, send a POST request to \/api/reviews/\.
- To retrieve all reviews, send a GET request to \/api/reviews/\.

## License
This project is open-source and available under the [MIT License](LICENSE).
cat