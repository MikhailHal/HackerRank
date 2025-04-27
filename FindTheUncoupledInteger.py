def getWays(n, coins):
    # dp[i] = 金額iを作る方法の数
    dp = [0] * (n + 1)
    dp[0] = 1  # 基本ケース: 0円を作る方法は1通り(何も選ばない)
    
    for coin in coins:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]
    
    return dp[n]