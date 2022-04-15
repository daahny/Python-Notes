# Program to print the fibonacci series upto n_terms
  
# Recursive function
def recursive_fibonacci(n):
   if n <= 1:
       return n
   else:
       a = recursive_fibonacci(n-1)
       b = recursive_fibonacci(n-2)
       return(a + b)
   
n_terms = int(input('enter: '))
   
# check if the number of terms is valid
if n_terms <= 0:
   print("Invalid input ! Please input a positive value")
else:
   print("Fibonacci series:")
   for i in range(n_terms):
       print(recursive_fibonacci(i))


# recursive_fibonacci(4)
#   --> a = recursive_fibonacci(3)
#       --> a = recursive_fibonacci(2)
#           --> a = recursive_fibonacci(1)
#           --> a = 1
#           --> b = recursive_fibonacci(0)
#           --> b = 0
#       --> a = 1
#       --> b = recursive_fibonacci(1)
#       --> b = 1
#   --> a = 2
#   --> b = recursive_fibonacci(2)
#       --> a = recursive_fibonacci(1)
#       --> a = 1
#       --> b = recursive_fibonacci(0)
#       --> b = 0
#   --> b = 1
# 







