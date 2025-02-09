// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.10;


// Import AirSwap Protocol
import "https://github.com/airswap/airswap-protocols/blob/master/source/swap/contracts/interfaces/ISwap.sol";

contract TradeExecutorAirSwap {
    ISwap public airSwap;

    constructor(address _airSwapAddress) {
        airSwap = ISwap(_airSwapAddress);
    }

    function executeTrade(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut
    ) public {
        // Create order
        ISwap.Order memory order = ISwap.Order({
            nonce: 0,
            expiry: block.timestamp + 3600,
            signerWallet: msg.sender,
            signerToken: tokenIn,
            signerAmount: amountIn,
            senderWallet: address(this),
            senderToken: tokenOut,
            senderAmount: amountOut,
            v: 0,
            r: bytes32(0),
            s: bytes32(0)
        });

        // Execute trade
        airSwap.swap(order);
    }
}