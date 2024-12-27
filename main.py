def f(n, k, dp_bool, dp_string):
    # Base case
    if k == 1:
        return n==4

    # Check if the result is already computed
    if (n, k) in dp_bool:
        return dp_bool[(n, k)]

    # Initialize the result as False
    res_bool = False
    res_string = ""
    # 합: 1 ~ n/2
    # 곱: 1 ~ sqrt(n) 중 약수
    # 차: 1 ~ (n-1) 개로 만들 수 있는 최대값 - very sparse
    # 제: 1 ~ (n-1) 개로 만들 수 있는 최대값 - very sparse
    # 주어진 k 에 대해 k 개로 만들 수 있는 수들의 집합을 만들고 이 안에서 순회.
    
    # Loop through all possible values of i and j for the summations
    for i in range(1, 200):
      # loop 범위 pow4
        for j in range(1, k):
            if i < n:  # To avoid negative n-i
                res_bool = f(i, j, dp_bool, dp_string) and f(n - i, k - j, dp_bool, dp_string)
                if(res_bool):
                  dp_bool[(n, k)] = True
                  res_string = f"({dp_string[(i, j)]} + {dp_string[(n - i,k - j)]})"
                  dp_string[(n, k)] = res_string
                  return True

            res_bool = f(i, j, dp_bool, dp_string) and f(n + i, k - j, dp_bool, dp_string)
            if(res_bool):
              dp_bool[(n, k)] = True
              res_string = f"({dp_string[(n + i,k - j)]} - {dp_string[(i, j)]})"
              dp_string[(n, k)] = res_string
              return True

            res_bool = f(i, j, dp_bool, dp_string) and f(n * i, k - j, dp_bool, dp_string)
            if(res_bool):
              dp_bool[(n, k)] = True
              res_string = f"({dp_string[(n * i,k - j)]} / {dp_string[(i, j)]})"
              dp_string[(n, k)] = res_string
              return True

            if n % i == 0:  # Check if division is valid
                res_bool = f(i, j, dp_bool, dp_string) and f(n // i, k - j, dp_bool, dp_string)
                if(res_bool):
                  dp_bool[(n, k)] = True
                  res_string = f"({dp_string[(i, j)]} * {dp_string[(n // i, k - j)]})"
                  dp_string[(n, k)] = res_string
                  return True

    # Store the result in memoization dictionary
    dp_bool[(n, k)] = False
    dp_string[(n, k)] = "impossible"
    return False

# Wrapper function to handle memoization and provide an easy interface
def calculate_f(n, k):
    dp_bool = {}
    dp_string = {}
    dp_string[(4, 1)] = "4"
    f(n, k, dp_bool, dp_string)
    return dp_string[(n, k)]

# Example usage
# n = 64 # Change to desired n
# k = 5 # Change to desired k
# print(calculate_f(n, k))

for i in range(100):
  print(f"{i}: {calculate_f(i, 5)}")
