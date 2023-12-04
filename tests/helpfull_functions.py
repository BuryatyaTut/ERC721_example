from brownie import accounts, bearsNFT, Contract, exceptions

def getMaxMintAmount():
    return 3

def getMintPrice():
    return 10 ** 15

def getMaxTokensPerAddress():
    return 6

def getTotalSupplyLimit():
    return 100
