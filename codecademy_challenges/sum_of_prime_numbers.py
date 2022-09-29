def sum_of_prime_factors(n):
    found_number = 0
    for number in range(2, n + 1):
        if n % number == 0:
            for i in range(2, number):
                if (number % i) == 0:  
                    break  
            else:  
                found_number += number
    return (found_number)  


print(sum_of_prime_factors(91))