# sources:
# Variation of class lecture: https://github.com/DURepo/CS_325_Exercises/blob/main/DynamicProgramming-lcs_bottomup.py
# Variation of class lecture: https://github.com/DURepo/CS_325_Exercises/blob/main/DynamicProgramming-lcs_bruteforce.py

# Time complexity: O(m*n)
def checkPalindrome_1(string, k):
    """
    Variation of class lecture LCS technique used as a template. Configured to deal with 
    https://github.com/DURepo/CS_325_Exercises/blob/main/DynamicProgramming-lcs_bottomup.py
    """
    string2 = string[::-1]
    m = len(string)
    n = len(string2)

    # create a 2-D dynamic programming table of size m+1 X n+1
    dp = [[0 for x in range(n+1)] for x in range(m+1)]

    # building the matrix
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif string[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j]= max(dp[i-1][j] , dp[i][j-1])

    hold = dp[m][n]
    if len(string) - hold <= k:
        return True
    else:
        return False


# Time complexity: O(2^n)
def checkPalindrome_2_helper(s1, s2, m,n):
    """
    Helper Function for checkPalindrome_2. Does recursive calls.
    """
    if m < 0 or n < 0:
        return 0
    elif s1[m] == s2[n]:
        return 1 + checkPalindrome_2_helper(s1, s2, m - 1, n - 1)
    else:
        return max(checkPalindrome_2_helper(s1, s2, m - 1, n), checkPalindrome_2_helper(s1, s2, m, n - 1))

def checkPalindrome_2(string, k):
    """
    Variation of class lecture: https://github.com/DURepo/CS_325_Exercises/blob/main/DynamicProgramming-lcs_bruteforce.py
    """
    string2 = string[::-1]
    hold = checkPalindrome_2_helper(string,string2, len(string)-1, len(string2)-1)
    print("this is hold ", len(string), hold)
    if len(string) - hold <= k:
        return True
    else:
        return False


s = "abcdeba"
k = 4
answer = checkPalindrome_1(s, k)
print(answer)

answer = checkPalindrome_2(s, k)
print(answer)

