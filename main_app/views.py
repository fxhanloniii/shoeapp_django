from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Shoe
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoes'] = Shoe.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class CollectionList(TemplateView):
    template_name = 'collection_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collection'] = Shoe.objects.filter(user=self.request.user)
        return context
    
@method_decorator(login_required, name='dispatch')
class ShoeCreate(CreateView):
    model = Shoe
    fields = ['brand', 'name', 'size', 'price', 'description', 'image_url']
    template_name = 'shoe_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('shoe_detail', kwargs={'pk': self.object.pk})


class ShoeDetail(DetailView):
    model = Shoe
    template_name = 'shoe_detail.html'

@method_decorator(login_required, name='dispatch')
class ShoeUpdate(UpdateView):
    model = Shoe
    fields = ['brand', 'name', 'size', 'price', 'description', 'image_url']
    template_name = 'shoe_update.html'

    def get_success_url(self):
        return reverse('shoe_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')   
class ShoeDelete(DeleteView):
    model = Shoe
    template_name = 'shoe_delete_confirmation.html'
    success_url = '/'

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("collection_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
