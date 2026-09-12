def find_primes_up_to_n(n):
    primes = []
    
    # 0 and 1 are not prime numbers, so we start from 2
    for num in range(2, n + 1):
        is_prime = True
        
        # Check for factors up to the square root of the number
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break  # Not a prime, stop checking this number
                
        if is_prime:
            primes.append(num)
            
    return primes

# Example usage:
N = 50
print(f"Prime numbers between 1 and {N}: {find_primes_up_to_n(N)}")
