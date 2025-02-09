// SPDX-License-Identifier: MIT
// Copyright (c) 2023 [Victoria Gong]

// Import Uniswap V3 Interfaces, for LFJ
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