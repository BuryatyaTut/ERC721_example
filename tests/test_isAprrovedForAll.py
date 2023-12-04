from brownie import accounts, bearsNFT, Contract, exceptions
from helpfull_functions import getMintPrice


def test_isApprovedForAll():
    account1 = accounts[0]
    account2 = accounts[1]
    contract = bearsNFT.deploy({'from': account1})

    # Test if an operator is approved for all tokens of an owner
    assert not contract.isApprovedForAll(account1, account2)