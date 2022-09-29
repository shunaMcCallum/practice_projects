def prime_finder(num):
    for number in range (2, num + 1):  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  

prime_finder(11)

# Else statement is situated OUTSIDE of the second for loop, because when it's inside it prints every check that's done of the two numbers
# together if there's a remainder
# When it's situated outside, the program has to go outside of the loop to know what to do when there is a remainder, so this naturally breaks
# the program out, it prints the required number and takes us back to the top of the FIRST for loop

# IF THE ELSE STATEMENT WERE INSIDE THE SECOND FOR LOOP THIS IS WHAT WOULD HAPPEN:
# range 2 - 12

# number = 2
# i = 2
# 2 % 2 == 0   --->   YES - break

# number = 3
# i = 2   /   3 % 2 == 1   ---> NO - print 3
# i = 3   /   3 % 3 == 0   ---> YES - break

# number = 4
# i = 2   /   4 % 2 == 0   ---> YES - break

# number = 5
# i = 2   /   5 % 2 == 1   ---> NO - print
# i = 3   /   5 % 3 == 2   ---> NO - print
# i = 4   /   5 % 4 == 1   ---> NO - print
# i = 5   /   5 % 5 == 0   ---> YES - break

# number = 6
# i = 2   /   6 % 2 == 0   ---> YES - break

# number = 7
# i = 2   /   7 % 2 == 1   ---> NO - print
# i = 3   /   7 % 3 == 1
# i = 4   /   7 % 4 == 3
# i = 5   /   7 % 5 == 2
# i = 6   /   7 % 6 == 1
# i = 7   /   7 % 7 == 0   ---> YES - break