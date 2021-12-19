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

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)

def test_wallet_set_up_fixture(empty_wallet):
    assert empty_wallet.balance == 0, "creates a new wallet"

def test_wallet_set_up(empty_wallet):
    assert empty_wallet.balance == 0, "creates a new wallet"

def test_transactions_empty(wallet):
    assert wallet.transactions == []
    assert wallet.balance == 20, "creates a new wallet"

def test_wallet_deposit(wallet):
    wallet.transaction("Deposit",10)
    assert wallet.balance == 30

#@freeze_time("2023-01-10")
def test_wallet_transaction(wallet):
    wallet.transaction("Deposit",10)
    assert wallet.transactions[0] == {'date':datetime.datetime.now().strftime('%Y-%m-%d'),'amount':10,'balance':30,'type':'Deposit'}

def test_wallet_withdraw():
    wallet = Wallet(100)
    wallet.transaction("Withdraw",20)
    assert wallet.balance == 80

def test_wallet_insufficient_funds():
    wallet = Wallet()    
    with pytest.raises(InsufficientAmount):
        wallet.transaction("Withdraw",100)


