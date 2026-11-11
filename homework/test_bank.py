
import pytest
import bank


@pytest.fixture
def account():
    return bank.BankAccount1("Nino")


def test_initial_balance(account):
    assert account.balance == 0.0


def test_deposit_success(account):
    account.balance = 100.0

    result = account.deposit(50.0)

    assert result == 150.0


@pytest.mark.parametrize("amount", [-50.0, 0])
def test_deposit_negative(account, amount):
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.deposit(amount)


def test_withdraw_success(account):
    account.balance = 200.0

    result = account.withdraw(50.0)

    assert result == 150.0


def test_withdraw_insufficient_funds(account):
    account.balance = 100.0

    with pytest.raises(ValueError, match="Balance is not enough"):
        account.withdraw(150.0)


@pytest.mark.parametrize("amount", [-50.0, 0])
def test_withdraw_negative(account, amount):
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.withdraw(amount)
