# Write a function, is_prime, that takes in a number as an argument. 
# The function should return a boolean indicating whether or not the given number is prime.

# A prime number is a number that is only divisible by two distinct numbers: 1 and itself.

# For example, 7 is a prime because it is only divisible by 1 and 7. 
# For example, 6 is not a prime because it is divisible by 1, 2, 3, and 6.

# You can assume that the input number is a positive integer.



#source code
def is_prime(n):
    c = 0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            c+=1
    if c==1:
        return True
    return False 

#check
output = is_prime(2)  # -> True
print(output)
output = is_prime(3) # -> True
print(output)
output = is_prime(4) # -> False
print(output)
output = is_prime(5) # -> True
print(output)
output = is_prime(5) # -> True
print(output)
output = is_prime(7) # -> True
print(output)
output = is_prime(8) # -> False
print(output)
output = is_prime(25) # -> False
print(output)
output = is_prime(31) # -> True
print(output)
output = is_prime(2017) # -> True
print(output)
output = is_prime(2048) # -> False
print(output)
output = is_prime(1) # -> False
print(output)
output = is_prime(713) # -> False
print(output)




