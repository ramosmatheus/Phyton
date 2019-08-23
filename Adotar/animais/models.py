from django.db import models

# Create your models here.


class Estado(models.Model):
    # nome_do_atributo = models.Tipo(configuração)
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.sigla + ' - ' + self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    descricao = models.TextField(
        blank=True, null=True, verbose_name='Descrição', help_text="Espaço para descrever sua cidade.")

    def __str__(self):
        return self.nome + ' - ' + self.estado.sigla + ' - ' + self.descricao


class Setor(models.Model):
    nome = models.CharField(max_length=50)
    diretor = models.CharField(max_length=50)

    def __str__(self):
        return self.nome + ' - ' + self.diretor


class Veiculo(models.Model):
    categoria = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.CharField(max_length=100)
    quilometragem = models.CharField(max_length=100)
    placa = models.CharField(max_length=100)

    def __str__(self):
        return self.categoria + ' - ' + self.marca + ' - ' + self.modelo + ' - ' + self.ano + ' - ' + self.quilometragem + ' - ' + self.placa


class Viagem(models.Model):
    quantidadePassageiros = models.IntegerField()
    finalidade = models.CharField(max_length=100)
    dataPartida = models.DateField(verbose_name='data de partida')
    dataRetorno = models.DateField(verbose_name='data de retorno')
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)

    def __str__(self):
        return self.quantidadePassageiros + ' - ' + self.finalidade + ' - ' + self.dataPartida + ' - ' + self.dataRetorno + ' - ' + self.veiculo


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    cargo = models.IntegerField("CPF")
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    cpf = models.IntegerField("CPF")
    cidade = models.ForeignKey(Cidade, on_delete= models.PROTECT ) 
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)
    viagem = models.ForeignKey(Viagem, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + ' - ' + self.email + ' - ' + str(self.cpf) + ' - ' + self.telefone
