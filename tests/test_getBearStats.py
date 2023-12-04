from brownie import accounts, bearsNFT, Contract, exceptions, reverts
from helpfull_functions import getMintPrice

def test_getBearStats():
    account = accounts[0]
    contract = bearsNFT.deploy({'from': account})

    # Test getting bear stats for existing bear
    contract.mint(1, {'from': account, 'value': getMintPrice()})
    tokenId = 0
    stats = contract.getBearsStats(tokenId)
    assert len(stats) == 3

    # Test getting bear stats for non-existing bear
    with reverts():
        contract.getBearsStats(9999)