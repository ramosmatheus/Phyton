from django.db import models

# Create your models here.

class Estado(models.Model):
    # nome_do_atributo = models.Tipo(configuração)
    sigla   = models.CharField(max_length=2)
    nome    = models.CharField(max_length=50)

    def __str__(self):
        return self.sigla + ' - ' + self.nome


class Cidade(models.Model):
    nome        = models.CharField(max_length=50)
    estado      = models.ForeignKey(Estado, on_delete= models.PROTECT )
    descricao   = models.TextField(blank=True, null=True, verbose_name='Descrição', help_text="Espaço para descrever sua cidade.")

    def __str__(self):
        return self.nome + ' - ' + self.estado.sigla + ' - ' + self.descricao

class Pessoa(models.Model):
    nome    = models.CharField(max_length=50)
    cpf     = models.IntegerField("CPF")
    email   = models.EmailField(max_length=100)
    cidade  = models.ForeignKey(Cidade, on_delete= models.PROTECT ) 

    def __str__(self):
        return self.nome + ' - ' + self.cidade.nome + ' - ' + self.email + ' - ' + str(self.cpf)        