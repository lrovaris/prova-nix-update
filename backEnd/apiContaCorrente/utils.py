from uuid import uuid4
import json
import sqlite3
import os.path
from .models import Client
from datetime import date



    # O nome deve ser auto explicatorio, mas ainda sim, essa é a declaração da função de update do banco de dados local
    # ela recebe 3 parametros, o primeiro é o novo valor do campo a ser editado, o segundo é o id unico do campo,
    # e o terceiro é o campo que será editado no banco de dados.
def updateSqliteTable(value, unique_id, field):

        # para fins de teste, se passo os campos erroneamente deve interromper a execução e retornar falso
        # logo chamo um validador de campos para ter certeza que esta tudo de acordo :3
    if(validaUpdate(value, field)):
        return False

    try:
        client = Client.objects.get(_id = unique_id)
        setattr(client, field, value)

        return True

    except sqlite3.Error as error:

        print("codigo nao atualizou, erro: ", error)

        return False


def register(_json):

        try:

            _json = json.loads(_json)
            client = Client(
                            _name = _json['_name'],
                            _balance = _json['_balance'],
                            _credit_line = _json['_credit_line'],
                            )

            client.save()
            return client._id


        # Se algo deu errado catch erro
        except sqlite3.Error as error:
            print("codigo nao atualizou, erro: ", error)
            return False



def realizaDebitoOuCredito(value, unique_id, field):

    client = Client.objects.get(_id = unique_id)

    newValue = getattr(client, field) + value

    setattr(client, field, newValue)

    client.save()

    funcao = (field == '_balance' and 'debito' or 'credito')

    transaction = Transaction()
    transaction._date = date.today(),
    transaction._type = funcao,
    transaction._value = value,
    transaction._saldo_credito = client._credit_line,
    transaction._saldo_debito = client._balance,
    transaction._description = f'Foi realizada uma funcao de {funcao} no valor de {value} no dia {date.today()}'

    json_transaction = json.dumps(transaction.__dict__,default=str)
    print(json_transaction)
    transaction_history = {}

    if client._transaction_history:
        transaction_history = json.loads(client._transaction_history)

        print(json_transaction, ' this is a transaction??')

        transaction_history.append(json_transaction)
        client._transaction_history = json.dumps(transaction_history, indent=0, default=str)
    else:
        client._transaction_history = json.dumps([json_transaction], indent=0, default=str)
    client.save()
    print(client._transaction_history, ' client._transaction_history')

    return getattr(client, field)


# -----------------------------------------------------------------------------------------------------------------------------------------------
# Funções de validação, não vou comentar muito sobre elas
# caso fique alguma duvida so me chamar

class Transaction(object):
        _date = 0
        _type = ""
        _value = 0
        _saldo_credito = 0
        _saldo_debito = 0
        _description = ''




def isValidField(field, value):
    return {
        '_balance': isinstance(value, int),
        '_name': isinstance(value, str),
        '_credit_line': isinstance(value, int),
        '_password': isinstance(value, str),
        '_personal_info': isinstance(value, str)
    }.get(field, False)





def validaUpdate(value, field):
    if(field == '_id'):
        print('Não pode mudar o _id.')
        return False
    if(isValidField(field, value)):
        return True
    else:
        print('Campo inexistente no banco de dados ou valor com tipo incorreto')
        return False

