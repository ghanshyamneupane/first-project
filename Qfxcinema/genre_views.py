from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Genre
from django.urls import reverse_lazy
from django.shortcuts import render

class GenreListView(ListView):
	model = Genre
	template_name = 'Qfxcinema/genre/create.html'
	context_object_name = 'Genre'


def genre_search(request):
	name = request.GET.get('name')
	genre = Genre.objects.filter(name__icontains=name)
	context = {

		'Genre' : genre
	}

	return render(request, 'Qfxcinema/genre/create.html', context)


class GenreDetailView(DetailView):
	model = Genre
	template_name = 'Qfxcinema/genre/create.html'
	context_object_name = 'Genre'


class GenreCreateView(CreateView):
	model = Genre
	template_name = 'genre/create.html'
	fields = '__all__'
	success_url = reverse_lazy('Qfxcinema:movie-list')

	def get_context_data(self, **kwargs):
		context = super(GenreCreateView, self).get_context_data(**kwargs)
		context = {
	    	'Create' : 'Create',
	    	'form'   : self.get_form(),
	    	'Create_Genre' : 'Create New Genre',
		}

		return context

class GenreUpdateView(UpdateView):
	model = Genre
	template_name = 'Qfxcinema/genre/create.html'
	fields = '__all__'
	success_url = reverse_lazy('Qfxcinema:genre-list')

	def get_context_data(self, **kwargs):
		context = super(GenreUpdateView, self).get_context_data(**kwargs)
		context = {
	    	'Update' : 'Update',
	    	'form'   :  self.get_form(),
	    	'Update_Genre' : 'Update This Genre',
	    }
		return context