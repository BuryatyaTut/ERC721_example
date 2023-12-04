from brownie import accounts, bearsNFT, Contract, exceptions
from helpfull_functions import getMintPrice

def test_approval():
    account1 = accounts[0]
    account2 = accounts[1]
    contract = bearsNFT.deploy({'from': account1})

    # Test approving a token transfer
    contract.mint(1, {'from': account1, 'value': getMintPrice()})
    tokenId = 0
    contract.approve(account2, tokenId, {'from': account1})
    assert contract.getApproved(tokenId) == account2

    # Test transferring a token after approval
    contract.transferFrom(account1, account2, tokenId, {'from': account2})
    assert contract.ownerOf(tokenId) == account2