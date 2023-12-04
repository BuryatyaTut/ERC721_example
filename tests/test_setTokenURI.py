from brownie import accounts, bearsNFT, Contract, exceptions, reverts
from helpfull_functions import getMintPrice

def test_setTokenURI():
    account = accounts[0]
    contract = bearsNFT.deploy({'from': account})

    # Test setting token URI for existing token
    contract.mint(1, {'from': account, 'value': getMintPrice()})
    tokenId = 0
    tokenURI = "ipfs://newTokenURI"
    contract.setTokenURI(tokenId, tokenURI, {'from': account})
    assert contract.tokenURI(tokenId) == tokenURI

    # Test setting token URI for non-existing token
    with reverts():
        contract.setTokenURI(9999, tokenURI, {'from': account})