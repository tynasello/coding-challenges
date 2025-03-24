import math


def tsdp(dist, D):
    n = len(dist)

    # dp[mask][i] = min distance visiting all cities in mask once (ending at city i)
    dp = [[math.inf] * n for _ in range(2**n)]

    # then dp[mask][i] = min(dp[mask \ i][j] + dist[j][i]) for all j in mask

    for i in range(n):
        dp[1 << i][i] = 0

    for mask in range(2**n):
        for i in range(n):
            if mask & (1 << i):
                for j in range(n):
                    if mask & (1 << j) and i != j:
                        dp[mask][i] = min(
                            dp[mask][i], dp[mask ^ (1 << i)][j] + dist[j][i]
                        )

    minCost = math.inf
    for i in range(n):
        minCost = min(minCost, dp[2**n - 1][i] + dist[i][0])
    return minCost <= D


def main():
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]  # dist[i][j] = weight from city i to j

    print(tsdp(dist, 80))
    print(tsdp(dist, 50))


if __name__ == "__main__":
    main()
