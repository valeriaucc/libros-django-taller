from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Autor, Libro
from .forms import AutorForm, LibroForm

# CRUD AUTORES (Function Based Views)

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'gestion/lista_autores.html', {'autores': autores})


def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'gestion/autor_form.html', {'form': form})


def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'gestion/autor_form.html', {'form': form})


def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'gestion/autor_confirm_delete.html', {'autor': autor})


# CRUD AUTORES (Class Based Views)

class AutorListView(ListView):
    model = Autor
    template_name = 'gestion/lista_autores.html'
    context_object_name = 'autores'


class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_create.html'
    success_url = reverse_lazy('lista_autores')


class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_update.html'
    success_url = reverse_lazy('lista_autores')


class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'gestion/autor_delete.html'
    success_url = reverse_lazy('lista_autores')


# CRUD LIBROS (Class Based Views)

class LibroListView(ListView):
    model = Libro
    template_name = 'gestion/lista_libros.html'
    context_object_name = 'libros'


class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/libro_create.html'
    success_url = reverse_lazy('lista_libros')


class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/libro_update.html'
    success_url = reverse_lazy('lista_libros')


class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'gestion/libro_delete.html'
    success_url = reverse_lazy('lista_libros')