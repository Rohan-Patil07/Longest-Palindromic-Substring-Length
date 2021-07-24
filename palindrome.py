# Python3 program for the above approach
 
# Function to obtain the length of
# the longest palindromic substring
def longestPalSubstr(str):
     
    # Length of given string
    n = len(str)
    # Stores the maximum length
    maxLength = 1
    start = 0
  
    # Iterate over the string
    for i in range(n):
  
        # Iterate over the string
        for j in range(i, n):
            flag = 0
  
            # Check for palindrome
            for k in range((j - i + 1) // 2):
                if (str[i + k] != str[j - k]):
                    flag = 1
  
            # If string [i, j - i + 1]
            # is palindromic
            if (flag != 1 and (j - i + 1) > maxLength):
                start = i
                maxLength = j - i + 1
             
    # Return length of LPS
    return (maxLength-1)
 
# Driver Code
 
# Given string
str1 = "level"
str2 = "abac"
  
# Function call
print(longestPalSubstr(str1))
print(longestPalSubstr(str2))
