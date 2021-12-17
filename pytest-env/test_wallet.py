import pytest
import wallet

def test_wallet_set_up():
    wallet = Wallet()
    assert wallet.balance == 0, "creates a new wallet"
