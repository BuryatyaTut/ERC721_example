from brownie import accounts, bearsNFT, Contract, exceptions
from helpfull_functions import getMintPrice

def test_balanceOf():
    account = accounts[0]
    contract = bearsNFT.deploy({'from': account})

    # Test balance after minting
    amount = 3
    contract.mint(amount, {'from': account, 'value': getMintPrice() * amount})
    assert contract.balanceOf(account) == amount