from django.contrib import admin
from . import livros, emprestimo, autor, perfil


# Register your models here.

admin.site.register(livros)
admin.site.register(emprestimo)
admin.site.register(autor)
admin.site.register(perfil)
