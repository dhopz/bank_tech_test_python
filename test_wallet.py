import pytest
from wallet import Wallet

def test_wallet_set_up():
    wallet = Wallet()
    assert wallet.balance == 0, "creates a new wallet"

def test_transactions_empty():
    wallet = Wallet()
    assert wallet.transactions == []

def test_wallet_intial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_depost():
    wallet = Wallet(100)
    wallet.deposit(10)
    assert wallet.balance == 110

    