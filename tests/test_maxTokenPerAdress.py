from brownie import accounts, bearsNFT, Contract, exceptions, reverts
from helpfull_functions import getMintPrice, getMaxTokensPerAddress, getMaxMintAmount

def test_maxTokensPerAddress():
    account = accounts[0]
    contract = bearsNFT.deploy({'from': account})

    # Test minting up to the maximum tokens per address
    contract.mint(getMaxMintAmount(), {'from': account, 'value': getMintPrice() * getMaxMintAmount()})
    contract.mint(getMaxMintAmount(), {'from': account, 'value': getMintPrice() * getMaxMintAmount()})
    assert contract.balanceOf(account) == getMaxTokensPerAddress()

    # Test minting more than the maximum tokens per address
    with reverts():
        contract.mint(1, {'from': account, 'value': getMintPrice()})