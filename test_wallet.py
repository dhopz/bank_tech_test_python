import datetime
import pytest
from wallet import Wallet, InsufficientAmount
# from freezegun import freeze_time


FAKE_TIME = datetime.datetime(2023, 1, 10)

@pytest.fixture
def patch_datetime_now(monkeypatch):

    class mydatetime:
        @classmethod
        def now(cls):
            return FAKE_TIME

    monkeypatch.setattr(datetime, 'datetime', mydatetime)

def test_patch_datetime(patch_datetime_now):
    assert datetime.datetime.now() == FAKE_TIME

def test_wallet_set_up():
    wallet = Wallet()
    assert wallet.balance == 0, "creates a new wallet"

def test_transactions_empty():
    wallet = Wallet()
    assert wallet.transactions == []

def test_wallet_intial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_deposit():
    wallet = Wallet(100)
    wallet.deposit(10)
    assert wallet.balance == 110

#@freeze_time("2023-01-10")
def test_wallet_transaction():
    wallet = Wallet(100)
    wallet.deposit(10)
    assert wallet.transactions[0] == {'date':datetime.datetime.now().strftime('%Y-%m-%d'),'amount':10,'balance':110}

def test_wallet_withdraw():
    wallet = Wallet(100)
    wallet.withdraw(20)
    assert wallet.balance == 80

def test_wallet_insufficient_funds():
    wallet = Wallet()    
    with pytest.raises(InsufficientAmount):
        wallet.withdraw(100)


