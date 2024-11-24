import sys
import math

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime

def main():
    input = sys.stdin.read
    data = input().split()
    
    limit = 246912  # 123456 * 2
    is_prime = sieve_of_eratosthenes(limit)

    results = []
    for n in map(int, data):
        if n == 0:
            break
        count = sum(is_prime[n + 1:2 * n + 1])  # n < x <= 2n
        results.append(count)
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
