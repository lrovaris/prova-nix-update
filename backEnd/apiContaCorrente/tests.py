from django.test import TestCase
from . import views
import django.http
import pytest

def test_update_campo_vazio():
    assert views.validaUpdate(0, '') == False

def test_update_balance_correto():
    assert views.validaUpdate(0, '_balance') == True

def test_fail_update_balance_type():
    assert views.validaUpdate('0', '_balance') == False

def test_update_credit_line_correto():
    assert views.validaUpdate(0, '_credit_line') == True

def test_fail_update_credit_line_type():
    assert views.validaUpdate('0', '_credit_line') == False

def test_update_password_correto():
    assert views.validaUpdate('46070d4bf934fb0d4b06d9e2c46e346944e322444900a435d7d9a95e6d7435f5', '_password') == True

def test_fail_update_password_type():
    assert views.validaUpdate(0, '_password') == False

def test_update_name_correto():
    assert views.validaUpdate('name', '_name') == True

def test_fail_update_name_type():
    assert views.validaUpdate(0, '_name') == False


