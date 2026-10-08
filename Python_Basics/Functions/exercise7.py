def is_prime(number):
    if number <= 1:
        return False


    for i in range(2, number):
        if number % i == 0:
            return False

    return True



def filter_primes(number_list):
    prime_list = []


    for number in number_list:
        if is_prime(number):
            prime_list.append(number)


    return prime_list



my_list = [1, 4, 6, 7, 13, 9, 67]
result = filter_primes(my_list)


print("Original list:", my_list)
print("Prime numbers found:", result)