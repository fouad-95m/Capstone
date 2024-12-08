from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from .filters import ReviewFilter

# Movie Views
class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Review Views
class ReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ReviewFilter
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

# SignUp view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('index')  # Change 'index' to your desired redirect URL after signup
        else:
            messages.error(request, "There was an error during registration.")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('index')  # Change 'index' to your desired redirect URL after login
            else:
                messages.error(request, "Invalid credentials.")
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    return redirect('index')  # Change 'index' to your desired redirect URL after logout

# Review List View (class-based)
class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'

# Review Detail View
class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'

# Review Create View
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['movie', 'rating', 'content']
    template_name = 'reviews/review_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('review_detail', kwargs={'pk': self.object.pk})

# Review Update View
class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['movie', 'rating', 'content']
    template_name = 'reviews/review_form.html'

    def get_success_url(self):
        return reverse_lazy('review_detail', kwargs={'pk': self.object.pk})

# Review Delete View
class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_confirm_delete.html'
    success_url = reverse_lazy('review_list')  # Redirect to the review list after deletion

# List reviews for a specific movie
class MovieReviewsListView(ListView):
    model = Review
    template_name = 'reviews/movie_reviews_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Review.objects.filter(movie_id=movie_id)

# reviews/views.py

from django.shortcuts import render

# Define the index view for the root path
def index(request):
    return render(request, 'index.html')  # You can create a simple index template
