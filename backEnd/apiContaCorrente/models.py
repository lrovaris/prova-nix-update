from django.db import models
from uuid import uuid4
from jsonfield import JSONField


class Client (models.Model):
        # ID unico do cliente, utilizando o default da lib uuid4 geramos um id unico para o nosso cliente cujo serve tambem como chave primaria.
        # e nao pode ser editado
    _id = models.UUIDField(primary_key = True, default = uuid4, editable = False)

        # Nome do cliente, podem ter nomes repetidos, deve ser uma simples string.
    _name = models.CharField (max_length=255)

        # Saldo do cliente para uso de debito, deve ser um numero inteiro onde os dois ultimos numero representam as casas decimais
        # ou seja se o saldo em conta de um cliente é 17,65 _balance deve ser 1765.
    _balance = models.IntegerField ()

        # Linha de credito do cliente, saldo utilizado para transações em credito, deve ser um numero inteiro onde os dois ultimos numero representam as casas decimais
        # ou seja se a linha de credito de um cliente é 17,65 _balance deve ser 1765.
    _credit_line = models.IntegerField ()




        # TODO transformar isso em algo mais proximo do real
    _transaction_history = JSONField(default = None )


