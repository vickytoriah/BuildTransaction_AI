// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.10;

// Import LFG Swap Interface
import "https://github.com/LooksFarGood/lfg-swap/blob/main/contracts/interfaces/ILFGSwap.sol";

contract TradeExecutorLFG {
    ILFGSwap public lfgSwap;

    constructor(address _lfgSwapAddress) {
        lfgSwap = ILFGSwap(_lfgSwapAddress);
    }

    function executeTrade(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin
    ) public {
        // Approve token transfer
        IERC20(tokenIn).approve(address(lfgSwap), amountIn);

        // Execute trade
        lfgSwap.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            [tokenIn, tokenOut],
            msg.sender,
            block.timestamp + 3600
        );
    }
}