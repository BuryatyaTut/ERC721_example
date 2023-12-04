from brownie import accounts, bearsNFT, Contract, exceptions, reverts
from helpfull_functions import getMintPrice

def test_tokenURI():
    account = accounts[0]
    contract = bearsNFT.deploy({'from': account})

    # Test getting token URI for existing token
    contract.mint(1, {'from': account, 'value': getMintPrice()})
    tokenId = 0
    assert len(contract.tokenURI(tokenId)) == 0

    # Test getting token URI for non-existing token
    with reverts():
        contract.tokenURI(9999)