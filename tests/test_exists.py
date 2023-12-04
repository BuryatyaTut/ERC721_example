from brownie import accounts, bearsNFT, Contract, exceptions
from helpfull_functions import getMintPrice

# def test_exists():
#     account = accounts[0]
#     contract = bearsNFT.deploy({'from': account})

#     # Test existence of a token after minting
#     tokenId = contract.mint(1, {'from': account, 'value': getMintPrice()})
#     assert contract._exists(tokenId)