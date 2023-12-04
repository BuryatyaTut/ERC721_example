from brownie import accounts, bearsNFT, Contract, exceptions
from helpfull_functions import getMintPrice

def test_ownerOf():
    account = accounts[0]
    contract = bearsNFT.deploy({'from': account})

    # Test owner of a token after minting
    contract.mint(1, {'from': account, 'value': getMintPrice()})
    tokenId = 0
    assert contract.ownerOf(tokenId) == account