class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        
        pal = [[False]*n for _ in range(n)]

        for ln in range(1,n+1):
            for i in range(0,n-ln+1):
                j = i +ln-1

                if ln ==1:
                    pal[i][j]=True
                elif ln ==2:
                    pal[i][j]=s[i]==s[j]
                else:
                    pal[i][j] = s[i]==s[j] and pal[i+1][j-1]

        dp = [0] * (n+1)

        for i in range(n):
            dp[i+1]=max(dp[i+1],dp[i])

            for j in range(0, i+1):
                ln = i - j +1
                if ln >=k and pal[j][i]:
                    dp[i+1]=max(dp[i+1], dp[j]+1)

        return dp[n]


        