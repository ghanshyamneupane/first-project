from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Tag
from django.urls import reverse_lazy
from django.shortcuts import render

class TagListView(ListView):
	model = Tag
	template_name = 'Qfxcinema/tags/create.html'
	context_object_name = 'Tag'


def tag_search(request):
	name = request.GET.get('name')
	tag = Tag.objects.filter(name__icontains=name)
	context = {

		'Tag' : Tag
	}

	return render(request, 'Qfxcinema/tags/create.html', context)


class TagDetailView(DetailView):
	model = Tag
	template_name = 'Qfxcinema/tags/create.html'
	context_object_name = 'Tag'


class TagCreateView(CreateView):
	model = Tag
	template_name = 'tags/create.html'
	fields = '__all__'
	success_url = reverse_lazy('Qfxcinema:movie-list')

	def get_context_data(self, **kwargs):
		context = super(TagCreateView, self).get_context_data(**kwargs)
		context = {
			'Create' : 'Create',
			'form'   : self.get_form(),
			'Create_Genre' : 'Create New Genre',
		}

		return context

class TagUpdateView(UpdateView):
	model = Tag
	template_name = 'tags/create.html'
	fields = '__all__'
	success_url = reverse_lazy('Qfxcinema:genre-list')

	def get_context_data(self, **kwargs):
		context = super(TagUpdateView, self).get_context_data(**kwargs)
		context = {
			'Update' : 'Update',
			'form'   :  self.get_form(),
			'Update_Tag' : 'Update This Tag',
		}
		return context