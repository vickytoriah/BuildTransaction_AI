// SPDX-License-Identifier: MIT
// Copyright (c) 2023 [Victoria Gong]

// Import Flare FTSO Interface
import "https://github.com/flare-foundation/ftso-solidity/blob/main/contracts/FtsoV2Interface.sol";

contract TradeExecutor {
    FtsoV2Interface public ftso;

    constructor(address _ftsoAddress) {
        ftso = FtsoV2Interface(_ftsoAddress);
    }

    function getVerifiedPrice(string memory symbol) public view returns (uint256) {
        (uint256 price, ) = ftso.getCurrentPrice(symbol);
        return price;
    }

    function executeTrade(string memory symbol, uint256 amount) public {
        uint256 price = getVerifiedPrice(symbol);
        // Execute trade logic using verified price
    }
}

// Import Uniswap V3 Interfaces
import "@uniswap/v3-core/contracts/interfaces/IUniswapV3Pool.sol";
import "@uniswap/v3-core/contracts/libraries/TickMath.sol";
import "@uniswap/v3-core/contracts/libraries/FixedPoint96.sol";

contract TradeVerifierUniV3 {
    IUniswapV3Pool public uniswapPool;

    constructor(address _uniswapPoolAddress) {
        uniswapPool = IUniswapV3Pool(_uniswapPoolAddress);
    }

    function getSqrtPriceX96() public view returns (uint160) {
        (uint160 sqrtPriceX96, , , , , , ) = uniswapPool.slot0();
        return sqrtPriceX96;
    }

    function getPrice(address tokenIn, address tokenOut) public view returns (uint256) {
        uint160 sqrtPriceX96 = getSqrtPriceX96();
        uint256 price = (uint256(sqrtPriceX96) * uint256(sqrtPriceX96) * 1e18) >> (96 * 2);
        return price;
    }
}