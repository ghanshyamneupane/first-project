from django.urls import path, include
from .movie_views import MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView, movie_search, rating_create, MovieDeleteView
from .genre_views import GenreListView, GenreDetailView, GenreCreateView, GenreUpdateView, genre_search
from Qfxcinema.user_views import UserRegisterView, UserProfileView
from .tag_views import TagListView, TagDetailView, TagCreateView, TagUpdateView, tag_search
from .language_views import LanguageCreateView, LanguageListView, LanguageUpdateView, LanguageDeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

app_name = 'Qfxcinema'

urlpatterns = [

    path('', MovieListView.as_view(), name='movie-list'),
    path('search/', movie_search, name='movie_search'),
    path('create/', MovieCreateView.as_view(), name='movie-create'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('<int:pk>/update/', MovieUpdateView.as_view(), name='movie-update'),
    path('<int:pk>/delete/', MovieDeleteView.as_view(), name='movie-delete'),

    path('', GenreListView.as_view(), name='genre-list'),
    path('genre/search/', genre_search, name='genre_search'),
    path('create/genre/', GenreCreateView.as_view(), name='genre-create'),
    path('genre/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),
    path('genre/<int:pk>/update/', GenreUpdateView.as_view(), name='genre-update'),

    path('', TagListView.as_view(), name='tag-list'),
    path('search/', genre_search, name='tag_search'),
    path('create/tag/', TagCreateView.as_view(), name='tag-create'),
    path('<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('tag/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),

    path('user/register/', UserRegisterView.as_view(), name='user_register'),
    path('user/profile/', UserProfileView.as_view(), name='user-detail'),
    path('user/login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('user/logout/', LogoutView.as_view(next_page='/movie'), name='logout'),



    path('language/create/', LanguageCreateView.as_view(), name='language-create'),
    path('language/list/', LanguageListView.as_view(), name='language-list'),
    path('language/<int:pk>/update/', LanguageUpdateView.as_view(), name='language-update'),
    path('language/<int:pk>/delete/', LanguageDeleteView.as_view(), name='language-delete'),

    path('rating/create/', rating_create, name='movie_rating')
]
