from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import NappingForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
# Create your views here.


def home(request):
    return HttpResponse('this is home')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    seeds_finch_doesnt_have = Seed.objects.exclude(
        id__in=finch.seeds.all().values_list('id')
    )
    napping_form = NappingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'napping_form': napping_form,
        'seeds': seeds_finch_doesnt_have
    })


def add_napping(request, finch_id):
    form = NappingForm(request.POST)
    if form.is_valid():
        new_napping = form.save(commit=False)
        new_napping.finch_id = finch_id
        new_napping.save()
    return redirect('detail', finch_id=finch_id)


class SeedList(ListView):
    model = Seed


class SeedDetail(DetailView):
    model = Seed


class SeedCreate(CreateView):
    model = Seed
    fields = '__all__'


class SeedUpdate(UpdateView):
    model = Seed
    fields = ['name']


class SeedDelete(DeleteView):
    model = Seed
    success_url = '/seeds/'


class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'size', 'color', 'behavior']


class FinchUpdate(UpdateView):
    model = Finch
    fields = ['size', 'color', 'behavior']


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'


def assoc_seed(request, finch_id, seed_id):
    Finch.objects.get(id=finch_id).seeds.add(seed_id)
    return redirect('detail', finch_id=finch_id)
