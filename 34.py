 num_str = input("Adj meg egy szamot")
 num_int=int(num_str)
 even_count=0
 odd_count=0
 even_sum=0
 odd_sum=0 


while num_int !=0:
   num_str = input("Adj meg megegy szamot")
   num_int=int(num_str)
   for num_int in num_str: 
       if num_int%2 == 0: 
           even_count += 1
       else: 
           odd_count +=1


print("")
print("Sum of odds:", odd_sum)
print("Sum of evens:", even_sum)
print("Even count:", even_count)
print("Odd count:", odd_count)
print("Total positive int count:")
