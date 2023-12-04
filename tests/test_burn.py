from brownie import accounts, bearsNFT, exceptions
from helpfull_functions import getMintPrice

# def test_burn():
#     account = accounts[0]
#     contract = bearsNFT.deploy({'from': account})

#     # Test burning a token
#     tokenId = contract.mint(1, {'from': account, 'value': getMintPrice()})
#     contract._burn(tokenId, {'from': account})
    
#     # Test if the token exists after burning
#     with exceptions.VirtualMachineError():
#         assert not contract._exists(tokenId)