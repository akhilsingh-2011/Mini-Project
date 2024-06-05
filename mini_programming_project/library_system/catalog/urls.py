from django.urls import path
from .views import BookList, BookDetail, MagazineList, MagazineDetail, MovieList, MovieDetail


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('magazines/', MagazineList.as_view(), name='magazine-list'),
    path('magazines/<int:pk>/', MagazineDetail.as_view(), name='magazine-detail'),
    path('movies/', MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
]
