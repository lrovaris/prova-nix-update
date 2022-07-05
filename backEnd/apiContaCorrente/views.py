from django.shortcuts import render
from . import utils
import json
from .models import Client
from django.http import JsonResponse


# TODO validação de usuarios repetidos
def cadastro(request):
        body_unicode = request.body.decode('utf-8')
        unique_id = utils.register(body_unicode)
        return JsonResponse({"message" : 'Novo cliente cadastrado com sucesso', "_id" : unique_id}, safe=False)

# TODO vale tanto para debido e credito
# adicionar validador de saldo para não permitir debito ou credito alem do saldo disponivel
def debito(request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        saldo = utils.realizaDebitoOuCredito(body['value'], body['_id'], '_balance')
        return JsonResponse({"message" : f'Débito realizado com sucesso novo saldo: {saldo}'}, safe=False)

def credito(request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        saldo = utils.realizaDebitoOuCredito(body['value'], body['_id'], '_credit_line')
        return JsonResponse({"message" : f'Crédito realizado com sucesso novo saldo: {saldo}'}, safe=False)

def extratoCliente(request, cliente_id):
    client = Client.objects.get(_id = cliente_id)
    body = json.loads(client._transaction_history)

    arr = []

    for item in body:
        arr.append(item)

    return JsonResponse(arr, safe=False)


