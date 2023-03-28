from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import autor, emprestimo, livros, perfil
from .forms import AutorForm, EmprestimoForm, LivroForm, PerfilForm

# Create your views here.

def lista_livros(request):
    livros = livros.objects.all()
    return render(request, 'livros.html', {'livros': livros})

def livros(request, pk):
    livros = get_object_or_404(livros, pk=pk)
    return render(request, 'livros_detail.html', {'livros': livros})

def autor_list(request):
    autors = autor.objects.all()
    return render(request, 'autor_list.html', {'autor': autor})

def autor_detail(request, pk):
    autor = get_object_or_404(autor, pk=pk)
    return render(request, 'autor_detail.html', {'autor': autor})

def loan_list(request):
    loans = Loan.objects.all()
    return render(request, 'loan_list.html', {'loans': loans})

def loan_detail(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    return render(request, 'loan_detail.html', {'loan': loan})

def loan_create(request, pk):
    livros = get_object_or_404(livros, pk=pk)
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.livros = livros
            loan.borrower = request.user.profile
            loan.save()
            messages.success(request, 'Empréstimo criado com sucesso.')
            return redirect('loan_detail', pk=loan.pk)
    else:
        form = LoanForm()
    return render(request, 'loan_form.html', {'form': form, 'livros': livros})


def loan_return(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    loan.return_date = timezone.now()
    loan.save()
    messages.success(request, 'Empréstimo devolvido com sucesso.')
    return redirect('loan_detail', pk=loan.pk)


def profile_detail(request):
    profile = request.user.profile
    return render(request, 'profile_detail.html', {'profile': profile})