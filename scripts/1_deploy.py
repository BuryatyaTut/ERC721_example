from scripts.generate_metadata import gen_metadata
from brownie import accounts, bearsNFT, network, Contract, config
from brownie.network import account

def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    nft = bearsNFT.deploy({"from": dev})

    amount = 3
    value = (10 ** 15) * amount
    nft.mint(amount, {"from": dev, "value": value})

    gen_metadata()
    