const hre = require("hardhat");

async function main() {
  const MyNFT = await hre.ethers.getContractFactory("MyNFT");
  const myNFT = await MyNFT.deploy();

  await myNFT.deployed();

  console.log("Contrato NFT implantado em:", myNFT.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
