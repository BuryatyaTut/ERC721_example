import json
import random
import requests
from brownie import bearsNFT, accounts, network, config

def gen_metadata():
    dev = accounts.add(config["wallets"]["from_key"])
    bearsnft = bearsNFT[len(bearsNFT) - 1]  # get the most recently deployed bearsNFT contract
    print(f"Using contract: {bearsnft.address}")

    hair_map = ["Fade", "Mohawk", "Box", "Empty"]
    clothes_map = ["Jacket", "Suit", "Military", "Empty"]
    boots_map = ["Nike", "Adidas", "New Balance", "Empty"]

    num_bears = bearsnft.getNumberOfBears()
    ipfs_images = get_ipfs_images()

    for token_id in range(num_bears):
        image_uri = random.choice(ipfs_images)
        hair, clothes, boots = bearsnft.getBearsStats(token_id)

        metadata = {
            "name": f"0xBear #{token_id}",
            "description": f"A randomly generated bear NFT! with token id {token_id}",
            "image": image_uri,
            "attributes": [
                {"trait_type": "Hair", "value": hair_map[hair]},
                {"trait_type": "Clothes", "value": clothes_map[clothes]},
                {"trait_type": "Boots", "value": boots_map[boots]},
            ],
        }

        pinata_url = pin_to_pinata(metadata)
        bearsnft.setTokenURI(token_id, f"https://ipfs.io/ipfs/{pinata_url}")

def get_ipfs_images():
    ipfs_folder_url = "https://ipfs.io/ipfs/Qmb8Guy7sL3i3GWKxaP62m98r8FgMQYoxnpapTmotCDzu1/bear-"
    image_urls = [f"{ipfs_folder_url}{str(x).zfill(4)}.png" for x in range(500)]
    return image_urls

def pin_to_pinata(metadata):
    pinata_api_url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    headers = {
        "pinata_api_key": config["pinata"]["pinata_api_key"],
        "pinata_secret_api_key": config["pinata"]["pinata_secret_api_key"],
    }
    response = requests.post(pinata_api_url, headers=headers, json=metadata)
    if response.status_code == 200:
        return response.json()["IpfsHash"]
    else:
        raise Exception(f"Failed to pin to Pinata: {response.content}")