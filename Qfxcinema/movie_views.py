from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie, MovieRating
from django.urls import reverse_lazy
from django.shortcuts import render
import datetime
from django.http import JsonResponse
from django.contrib.auth.models import User


class MovieListView(ListView):
    today = datetime.date.today()
    ten_days_ago = today - datetime.timedelta(days=10)
    model = Movie
    template_name = 'Qfxcinema/home.html'

    # context_object_name = 'Movies'

    def get_context_data(self, **kwargs):
        context = super(MovieListView, self).get_context_data(**kwargs)
        movies = Movie.objects.filter(release_date__gt=self.today)
        now_showing = Movie.objects.filter(release_date__range=(self.ten_days_ago, self.today))
        context = {'Movies': movies, 'now_showing_movies': now_showing}


        return context


def movie_search(request):
    name = request.GET.get('name')
    movies = Movie.objects.filter(name__icontains=name)
    context = {

        'Movies' : movies
    }

    return render(request, 'Qfxcinema/home.html', context)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'Qfxcinema/detail.html'

    def get(self, request, pk):
        movie_object = Movie.objects.get(pk=pk)
        if request.user.is_anonymous:
            return render(request, 'Qfxcinema/detail.html', {'Movie': movie_object})

        else:
            user_object = User.objects.get(username=self.request.user.username)
            rated_movie = user_object.rateduser.all()
            movie_filter = rated_movie.filter(movie=movie_object).exists()
            # get to return oject not queryset

            if movie_filter:
                rating = rated_movie.filter(movie=movie_object).get().rating
                context = {

                    'Movie': movie_object,
                    'rating': rating
                }
                return render(request, self.template_name, context)
            else:
                context = {

                    'Movie': movie_object
                }

                return render(request, self.template_name, context)


class MovieCreateView(CreateView):
    model = Movie
    template_name = 'Qfxcinema/create.html'
    fields = ('name', 'genre', 'release_date', 'cast', 'poster')
    success_url = reverse_lazy('Qfxcinema:movie-list')

    def get_context_data(self, **kwargs):
        context = super(MovieCreateView, self).get_context_data(**kwargs)
        context = {
            'Create' : 'Create',
            'form'   : self.get_form(),
            'Create_Movie' : 'Create New Movie',
        }

        return context

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'Qfxcinema/create.html'
    fields = '__all__'
    success_url = reverse_lazy('Qfxcinema:movie-list')

    def get_context_data(self, **kwargs):
        context = super(MovieUpdateView, self).get_context_data(**kwargs)
        context = {
            'Update' : 'Update',
            'form'   :  self.get_form(),
            'Update_Movie' : 'Update This Movie',
        }
        return context


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('Qfxcinema:movie-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

def rating_create(request):

    if request.method == "POST":
        pk = request.POST['pk']
        user = request.POST['user']
        rating = request.POST['rating']
        movie_object = Movie.objects.get(pk=pk)
        user_object = User.objects.get(username=user)
        rating_object = MovieRating.objects.create(
            movie=movie_object, user=user_object, rating=rating)
        rating_object.save()
        data = {

            'rating': rating
        }
        return JsonResponse(data)