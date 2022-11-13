from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import NewForm
from .filters import NewFilter
from django.urls import reverse_lazy
from .models import Author, New
from django.contrib.auth.models import User

class NewsList(ListView):

    model = New

    ordering = "-created"

    template_name = 'news.html'

    context_object_name = 'news'

    paginate_by = 2

    def get_queryset(self):

        queryset = super().get_queryset()

        self.filterset = NewFilter(self.request.GET, queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filterset'] = self.filterset
        return context



class NewDetail(DetailView):

    model = New

    template_name = 'new.html'

    context_object_name = 'new'

class NewSearch(NewsList):
    model = New
    template_name = 'search.html'
    context_object_name = 'news'


class NewCreate(CreateView):
    form_class = NewForm
    model = New
    template_name = 'create.html'

class NewEdit(UpdateView):
    form_class = NewForm
    model = New
    template_name = 'edit.html'


class NewDelete(DeleteView):
    model = New
    template_name = 'delete.html'
    success_url = reverse_lazy('new_list')

