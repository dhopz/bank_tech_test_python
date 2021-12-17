import datetime
import pytest
from statement import Statement
# from freezegun import freeze_time


FAKE_TIME = datetime.datetime(2023, 1, 10)

@pytest.fixture
def patch_datetime_now(monkeypatch):

    class mydatetime:
        @classmethod
        def now(cls):
            return FAKE_TIME

    monkeypatch.setattr(datetime, 'datetime', mydatetime)

def test_create_statement():
    transactions = [{'date': '2021-12-17', 'amount': 10, 'balance': 10, 'type': 'Deposit'},
        {'date': '2021-12-17', 'amount': 10, 'balance': 20, 'type': 'Deposit'},
        {'date': '2021-12-17', 'amount': 10, 'balance': 30, 'type': 'Deposit'}]
    statement = Statement()
    result = statement.create_statement(transactions)    

    assert result == 'date || credit || debit || balance\n2021-12-17 || 10 || || 10\n2021-12-17 || 10 || || 20\n2021-12-17 || 10 || || 30\n'

