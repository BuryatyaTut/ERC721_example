// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";


contract bearsNFT is ERC721, Ownable {
    uint8 private maxMintAmount = 3;
    uint8 private maxTokensPerAddress = 6;
    uint256 private mintPrice = 0.001 ether; //Thought: I've seen something about safeMath from Chainlink
    uint32 private totalSupplyLimit = 100;

    uint32 private totalSupply;
    uint private trairTypeCnt = 4;

    uint256 private nonce = 0;     

    mapping (uint256 => string) private _tokenURIs;

    //Thought: I tried to write uint8, but it didn't work out, because the keccak256 function can't work with uint8 *I tried to roll it to uint8*
    struct Bear {
        uint hair;
        uint clothes;
        uint boots;
    }
    Bear[] private bears;

    constructor() ERC721("0xBears", "BRS") {
        totalSupply = 0;
    }

    function mint(uint32 amount) public payable {
        require(amount <= maxMintAmount, "Cannot mint more than the maximum allowed");
        require(balanceOf(msg.sender) + amount <= maxTokensPerAddress, "Cannot own more than the maximum allowed");
        require(totalSupply + amount <= totalSupplyLimit, "Total supply limit reached");
        require(msg.value >= mintPrice * amount, "Ether value sent is not correct");

        for (uint32 i = 0; i < amount; ++i) {
            createNewRandomBear();
            totalSupply++; //Thought: I think for some reason it's more safe to increment totalSupply only after successfull bear creation 
        }
    }

    function createNewRandomBear() private returns (uint256) {
        uint256 newId = bears.length;
        //Thought: Maybe it's better to call random once and reuse it, to save gas
        uint hair = random() % trairTypeCnt;
        uint clothes = random() % trairTypeCnt;
        uint boots = random() % trairTypeCnt;

        bears.push(Bear(hair, clothes, boots));
        _safeMint(msg.sender, newId);
        return newId;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public onlyOwner {
        require(_exists(tokenId), "bearsNFTMetadata: URI set of nonexistent token");
        _tokenURIs[tokenId] = _tokenURI;
    }

    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "bearsNFTMetadata: URI query for nonexistent token");

        string memory _tokenURI = _tokenURIs[tokenId];
        return bytes(_tokenURI).length > 0 ? _tokenURI : super.tokenURI(tokenId);
    }

    function getNumberOfBears() public view returns (uint256) {
        return bears.length; 
    }

    function getBearsStats(uint256 tokenId) public view
        returns (uint, uint, uint)
    {
        return (bears[tokenId].hair, bears[tokenId].clothes, bears[tokenId].boots);
    }

    //Thought: It's better to use Chainlink random I guess
    function random() private returns (uint) {
        nonce++;
        return uint(keccak256(abi.encodePacked(block.timestamp, msg.sender, nonce)));
    }
}
