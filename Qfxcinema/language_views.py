from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Language
from django.urls import reverse_lazy


class LanguageCreateView(CreateView):
    model =Language
    template_name = 'language/create.html'
    fields = ('name', )
    success_url =reverse_lazy('Qfxcinema:movie-list')

    def get_context_data(self, **kwargs):
        context = super(LanguageCreateView, self).get_context_data(**kwargs)
        context['language'] = 'this is for language'
        return  context

class LanguageListView(ListView):
	model = Language
	template_name = 'language/create.html'
	context_object_name = 'Languages'


class LanguageUpdateView(UpdateView):
	model = Language
	template_name = 'language/update.html'
	fields = '__all__'
	success_url = reverse_lazy('Qfxcinema:language-list')

	def get_context_data(self, **kwargs):
		context = super(LanguageUpdateView, self).get_context_data(**kwargs)
		context['language']= 'this is for update'
		return context

class LanguageDeleteView(DeleteView):
	model = Language
	success_url = reverse_lazy('Qfxcinema:language_list')

	def get(self, request, *args, **kwargs):
		self.post(self, request, *args, **kwargs)