const hre = require("hardhat");

async function main() {
  const ZombieFactory = await hre.ethers.getContractFactory("ZombieFactory");
  const zombieFactory = await ZombieFactory.deploy();

  await zombieFactory.deployed();

  console.log("ZombieFactory deployed to:", zombieFactory.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
