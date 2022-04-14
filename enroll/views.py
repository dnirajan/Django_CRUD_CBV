from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import UserForm
from .models import User
from django.views.generic.base import TemplateView, RedirectView, View


# Create your views here.
class AddnshowView(TemplateView):
    template_name = 'addandshow.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = UserForm()
        stud = User.objects.all()
        context = {'form': fm, 'stu': stud}
        return context

    def post(self, request):
        fm = UserForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            mail = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=mail, password=pw)
            reg.save()
        return redirect('/')


# def addnshow(request):
#     if request.method == 'POST':
#         fm = UserForm(request.POST)
#         if fm.is_valid():
#             nm = fm.cleaned_data['name']
#             mail = fm.cleaned_data['email']
#             pw = fm.cleaned_data['password']
#             reg = User(name=nm, email=mail, password=pw)
#             reg.save()
#             fm = UserForm()
#             return redirect('/')
#     else:
#         fm = UserForm()
#     stud = User.objects.all()
#     return render(request, 'addandshow.html', {'form': fm, 'stu': stud})
class DeleteView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


# def delete(request, id):
#     if request.method == "POST":
#         pi = User.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/')
class UpdateView(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        fm = UserForm(instance=pi)
        return render(request, 'update.html', {'form': fm})

    def post(self, request, id):
        pi = pi = User.objects.get(pk=id)
        fm = UserForm(instance=pi)
        return redirect('/')

# def update(request, id):
#     if request.method == 'POST':
#         pi = User.objects.get(pk=id)
#         fm = UserForm(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#     else:
#         pi = User.objects.get(pk=id)
#         fm = UserForm(instance=pi)
#     return render(request, 'update.html', {'form': fm})
