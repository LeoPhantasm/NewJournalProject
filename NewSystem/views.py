from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView, DetailView
from .models import Entry
from django.urls import reverse_lazy
from .forms import EntryForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginRequiredMixin, CreateView):
	model = Entry
	form_class = EntryForm
	template_name = 'NewSystem/home.html'
	success_url = reverse_lazy('dashboard')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class Dashboard(LoginRequiredMixin, View):
	def get(self, request):
		allentry = Entry.objects.all()
		return render(request, 'NewSystem/dashboard.html', {'Entry': allentry})

class Index(TemplateView):
    template_name = 'NewSystem/index.html'

class SignUpView(View):
	def get(self, request):
		form = UserRegisterForm()
		return render(request, 'NewSystem/sign-in.html', {'form': form})

	def post(self, request):
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			form.save()
			user = authenticate(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1']
			)

			login(request, user)
			return redirect('dashboard')

		return render(request, 'NewSystem/sign-in.html', {'form': form})

class EditItem(LoginRequiredMixin, UpdateView):
	model = Entry
	form_class = EntryForm
	template_name = 'NewSystem/home.html'
	success_url = reverse_lazy('dashboard')
	

class DeleteItem(LoginRequiredMixin, DeleteView):
	model = Entry
	template_name = 'NewSystem/delete.html'
	success_url = reverse_lazy('dashboard')
	context_object_name = 'Entry'

