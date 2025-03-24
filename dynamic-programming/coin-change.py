'''
LeetCode 322. Coin Change

You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = [math.inf for _ in range(amount + 1)]
        # minCoins[i] = min coins needed to make sum of i
        minCoins[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    minCoins[i] = min(minCoins[i], minCoins[i-c] + 1)

        res = minCoins[amount]
        return res if res != math.inf else -1