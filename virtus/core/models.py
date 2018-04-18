from django.db import models


TIPO_ENDERECO = [
    ('RES', 'Residencial'),
    ('COM', 'Comercial'),
    ('COB', 'Cobrança'),
    ('ENT', 'Entrega'),
    ('OUT', 'Outro'),
]

class Cliente(models.Model):
    nomerazaosocial = models.CharField(verbose_name=u'Nome/Razao Social', max_length=255)
    email = models.EmailField(verbose_name=u'E-mail')
    telefone = models.CharField(max_length=255, verbose_name=u'Telefone', default='0')

    def __str__(self):
        return self.nomerazaosocial


class Endereco(models.Model):
    cliente_end = models.ForeignKey(
        Cliente, related_name="endereco", on_delete=models.CASCADE)
    tipo_endereco = models.CharField(
        max_length=3, null=True, blank=True, choices=TIPO_ENDERECO)
    cep = models.CharField(verbose_name=u'CEP', max_length=16, null=True, blank=True)
    logradouro = models.CharField(verbose_name=u'Logradouro', max_length=255, null=True, blank=True)
    numero = models.CharField(verbose_name=u'Numero', max_length=16, null=True, blank=True)
    bairro = models.CharField(verbose_name=u'Bairro', max_length=64, null=True, blank=True)
    complemento = models.CharField(verbose_name=u'Complemento', max_length=64, null=True, blank=True)

    def __str__(self):
        return self.logradouro
