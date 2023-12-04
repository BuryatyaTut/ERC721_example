from brownie import accounts, bearsNFT, Contract, exceptions, reverts
from helpfull_functions import getMintPrice

def test_safeTransferFrom():
    account1 = accounts[0]
    account2 = accounts[1]
    contract = bearsNFT.deploy({'from': account1})

    # Test safe transferring a token
    contract.mint(1, {'from': account1, 'value': getMintPrice()})
    tokenId0 = 0
    contract.safeTransferFrom(account1, account2, tokenId0, {'from': account1})
    assert contract.ownerOf(tokenId0) == account2

    # Test safe transferring a token without approval
    contract.mint(1, {'from': account1, 'value': getMintPrice()})
    tokenId1 = 1
    with reverts():
        contract.safeTransferFrom(account1, account2, tokenId1, {'from': account2})