from django.shortcuts import render, redirect, get_object_or_404
from .models import Biblioteca
from .forms import BibliotecaForm

#VISUALIZAR - read a lista de acervos do livro
def listar_acervo(request): #ler o acervo
    acervo = Biblioteca.objects.all().order_by('-data_publicacao')
    return render(request, 'listar_acervo.html', {'acervo': acervo})


# CADASTRO -> CREATE cadastro de livro
def cadastrar_livro(request): #cria livro no banco -> create
    if request.method == 'POST':
        cadastro = BibliotecaForm(request.POST)
        if cadastro.is_valid():
            cadastro.save()
            return redirect('listar_acervo')
    else:
        cadastro = BibliotecaForm()
    return render(request, 'cadastro_livro.html', {'cadastro': cadastro})


#UPDATE -> atualizar a lista de livros
def atualizar_livro(request, pk):
    livro = get_object_or_404(Biblioteca, pk = pk)
    if request.method == 'POST':
        cadastro = BibliotecaForm(request.POST, instance = livro)
        if cadastro.is_valid():
            cadastro.save()
            return redirect('listar_acervo')
    else:
        cadastro = BibliotecaForm()
        return render(request, 'atualizar.html', {'cadastro': cadastro, 'livro': livro})
    

# REMOVE -> remove o livro criado pelo user
def remove_livro(request, pk):
    livro = get_object_or_404(Biblioteca, pk = pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('deletar')
    return render(request, 'deletar.html', {'livro': livro})
    


            



