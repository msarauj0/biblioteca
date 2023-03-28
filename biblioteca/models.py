from django.db import models

class livros(models.Model):
    
    titulo = models.CharField("Titulo",max_length=200)
    autor = models.CharField('Autor', max_length=20)
    descricao = models.CharField("Descrição",max_length=250)
    editora = models.CharField("Editora",max_length=50)
    status = models.CharField('Status', max_length=20)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    img = models.ImageField("Imagem", upload_to='imagens', null=True, blank=True)
    
    def __str__(self):
        return self.titulo
    
class emprestimo(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    usuario = models.CharField('Usuario', max_length=20)
    data_emprestimo = models.DateField("Data de emprestimo")
    data_devolucao = models.DateField("Data de devolução")
    
    def __str__(self):
        return self.usuario
    
class autor(models.Model):
    nome = models.CharField('Autor', max_length=40)
    email = models.CharField('Usuario', max_length=50)
    data_cadastro = models.DateField("Data de cadastro")

    def __str__(self):
        return self.nome
    
class perfil(models.Model):
    nome = models.CharField('Autor', max_length=40)
    email = models.CharField('Usuario', max_length=50)
    avatar = models.ImageField("Avatar", upload_to='imagens', null=True, blank=True)
    usuario = models.CharField('Usuario', max_length=20)


