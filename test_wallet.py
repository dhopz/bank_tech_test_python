import pytest
from wallet import Wallet

def test_wallet_set_up():
    wallet = Wallet()
    assert wallet.balance == 0, "creates a new wallet"

def test_transactions_empty():
    wallet = Wallet()
    assert wallet.transactions == []
