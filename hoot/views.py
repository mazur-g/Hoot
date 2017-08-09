from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import user
from .forms import userForm


class userListView(ListView):
    model = user


class userCreateView(CreateView):
    model = user
    form_class = userForm


class userDetailView(DetailView):
    model = user


class userUpdateView(UpdateView):
    model = user
    form_class = userForm

