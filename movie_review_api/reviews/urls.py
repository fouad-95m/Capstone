from django.urls import path
from . import views

urlpatterns = [
    # CRUD for Reviews
    path('new/', views.ReviewCreateView.as_view(), name='review_create'),
    path('<int:pk>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('<int:pk>/edit/', views.ReviewUpdateView.as_view(), name='review_edit'),
    path('<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review_delete'),
    path('movie/<int:movie_id>/', views.MovieReviewsListView.as_view(), name='movie_reviews_list'),
]
