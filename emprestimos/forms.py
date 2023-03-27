from django.forms import ModelForm
from .models import livros, emprestimo, autor, perfil

class LivroForm(ModelForm):
    class Meta:
        model = livros
        fields = ['titulo', 'img', 'autor' , 'descricao', 'editora', 'status']        

class EmprestimoForm(ModelForm):
    class Meta:
        model = emprestimo
        fields = '_all_'
        
class AutorForm(ModelForm):
    class Meta:
        model = autor
        fields = '_all_'
        
class PerfilForm(ModelForm):
    class Meta:
        model = perfil
        fields = '_all_'        
        
