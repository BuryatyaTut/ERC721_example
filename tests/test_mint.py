from brownie import accounts, bearsNFT, Contract, exceptions, reverts
from helpfull_functions import getMintPrice, getMaxMintAmount

def test_mint():
    account = accounts[0]
    contract = bearsNFT.deploy({'from': account})

    # Test minting within limits
    contract.mint(1, {'from': account, 'value': getMintPrice()})
    assert contract.balanceOf(account) == 1

    # Test minting more than the maximum allowed
    with reverts():
        contract.mint(getMaxMintAmount() + 1, {'from': account, 'value': getMintPrice() * (getMaxMintAmount() + 1)})