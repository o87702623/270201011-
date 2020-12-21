def harmonic_sum(n):
    if n == 1:
      return n
    else:
      return 1 / n + harmonic_sum(n-1)

print(harmonic_sum(5))