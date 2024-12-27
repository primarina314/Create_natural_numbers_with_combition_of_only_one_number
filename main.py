dp = []
dp_done = []
for i in range(100):
  dp.append(set())
  dp_done.append(False)
dp_done[0] = dp_done[1] = True
dp[1].add(4)

def fill_up(k):
  # bottom-up approach
  if(k <= 1 | dp_done[k]):
    return
  fill_up(k-1)

  for i in range(1, k):
    # k//2
    for item1 in dp[i]:
      for item2 in dp[k-i]:
        dp[k].add(item1 + item2)
        dp[k].add((item1 - item2) if(item1 > item2) else (item2 - item1))
        # n is not negative, so don't need to consider negative elements in dp like -4.
        dp[k].add(item1 * item2)
        if(item2 > 0 and item1 % item2 == 0):
          dp[k].add(item1 // item2)
  dp_done[k] = True    
  return
fill_up(10)
print(sorted(dp[1]))
print(sorted(dp[2]))
print(sorted(dp[3]))
print(sorted(dp[4]))
print(sorted(dp[5]))
print(sorted(dp[6]))
print(sorted(dp[7]))
print(sorted(dp[8]))
print(sorted(dp[9]))
print(sorted(dp[10]))

print(len(dp[1]))
print(len(dp[2]))
print(len(dp[3]))
print(len(dp[4]))
print(len(dp[5]))
print(len(dp[6]))
print(len(dp[7]))
print(len(dp[8]))
print(len(dp[9]))
print(len(dp[10]))

dp_string = {}
dp_string[(4, 1)] = "4"

def f(n, k):
  # Check if the result is already computed
  if (n, k) in dp_string:
    return dp_string[(n, k)]
  
  # determine whether it's possible or not in advance
  if not n in dp[k]:
    dp_string[(n, k)] = "impossible"
    return dp_string[(n, k)]
  if k < 1:
    dp_string[(n, k)] = "impossible"
    return dp_string[(n, k)]

  # Loop through all possible values of i and j for the summations
  for j in range(1, k):
    for item in dp[j]:
      # summation
      if(item <= n//2):
        if((n - item) in dp[k - j]):
          dp_string[(n, k)] = "(" + f(item, j) + " + " + f(n - item, k - j) + ")"
          return dp_string[(n, k)]

      # substraction
      if(item >= n):
        if((item - n) in dp[k - j]):
          dp_string[(n, k)] = "(" + f(item, j) + " - " + f(item - n, k - j) + ")"
          return dp_string[(n, k)]

      # multiplication
      if(item > 0 and n > 0 and item * item <= n and n % item == 0):
        if((n // item) in dp[k - j]):
          dp_string[(n, k)] = "(" + f(item, j) + " * " + f(n // item, k - j) + ")"
          return dp_string[(n, k)]
      
      if(n == 0 and 0 in dp[k - j]):
        dp_string[(n, k)] = "(" + f(item, j) + " * " + f(0, k - j) + ")"
        return dp_string[(n, k)]

      # division
      if(item > 0 and n > 0 and item % n == 0):
        if((item // n) in dp[k - j]):
          dp_string[(n, k)] = "(" + f(item, j) + " / " + f(item // n, k - j) + ")"
          return dp_string[(n, k)]

  # Store the result in memoization dictionary
  # Actually, unreachable line
  dp_string[(n, k)] = "impossible"
  return dp_string[(n, k)]

# Wrapper function to handle memoization and provide an easy interface
def calculate_f(n, k):
    return f(n, k)

# Example usage
# n = 64 # Change to desired n
# k = 5 # Change to desired k
# print(calculate_f(n, k))

for i in range(500):
  print(f"{i}: {calculate_f(i, 6)}")
  calculate_f(i, 5)
