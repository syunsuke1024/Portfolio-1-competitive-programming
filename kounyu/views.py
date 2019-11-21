from django.shortcuts import render
from .forms import KounyuForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import Category,Kounyu,Shozoku,Shosha

class KounyuListView(ListView):
    model = Kounyu
    template_name = 'kounyu/kounyu_list.html'

    def queryset(selfself):
        return Kounyu.objects.all()

class KounyuCreateView(CreateView):
    model = Kounyu
    form_class = KounyuForm
    success_url = reverse_lazy('kounyu:create_done')

def create_done(request):
    return render(request,'kounyu/create_done.html')

class KounyuUpdateView(UpdateView):
    model = Kounyu
    form_class = KounyuForm
    success_url = reverse_lazy('kounyu:update_done')

def update_done(request):
    return render(request,'kounyu/update_done.htnl')

class KounyuDeleteView(DeleteView):
    model = Kounyu
    success_url = reverse_lazy('kounyu:delete_done')

def delete_done(request):
    return render(request, 'kounyu/delete_done.html')
