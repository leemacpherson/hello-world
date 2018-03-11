# this program takes the list of hex characters and adds them
# then negates each bit in the binary representation, then adds one to the result
# The binary value is then converted to hex and this is what is returned

# Ask for all of the hex values that will be added.  These values will be put in a list.
# A while-loop will be used to add all of the elements in the list

# make a list to store all of the values that have to be added
#set the first element of the list to 25 (hex 0x19) which always is used in every checksum

import random

def decmial2bin(decimal_sum):
        bin_sum = bin(decimal_sum)
        return (bin_sum)
        
dec_list = [25]
hex_value = int("0")

while hex_value != "":
        # change the hex value to decimal so the addition goes correctly
        hex_value = input ("enter the hex values you need to get 2-s complement for: ")
        print ("hex_value is :", hex_value)
        if hex_value == "":
                break
        dec_value = int(hex_value, 16)
        print ("decimal_value is :", dec_value)
        dec_list.append(dec_value)
 
# calculate the sum of all of the elements

print(" all of the values have been entered")
dec_sum = sum(dec_list)
print("the sum is: ", dec_sum)

# pass the sum to the function decmial2bin()

bin_sum = decmial2bin(dec_sum)
#print("the binary value is : ", bin_sum)
  
# use string operators to flip each bit in the binary number (can;t get negation to work)

length = len(bin_sum)
#print ("the length of bin_sum is ", length)
highest_index = length - 1
#print("highest_index is ", highest_index)

#convert the string bin_sum to list
bin_sum5 = list(bin_sum)
#print ("type of bin_sum5 is ", type(bin_sum5))

# removes the "0b" from the bin_sum5 value
bin_sum5.remove("b")
bin_sum5.remove("0")
print("the binary value is : ", bin_sum5)


#change each value in the list

i = highest_index - 2
#print ("i is ", i)
while i >= 0:
        #print ("bin_sum5 is ", bin_sum5[i])
        if bin_sum5[i] == "0":
                bin_sum5[i] = "1"
        else:
               bin_sum5[i] = "0"
        
        i -= 1
        #print ("i is ", i)
                 
print("the negated binary value is : ", bin_sum5)

#convert the string bin_sum5 to an integer

num = int(''.join(str(x) for x in bin_sum5), base=2)
print ("the integer value of the bin_sum5 list is: ", num)
#print ("type of num is ", type(num))

#add 1 to the integer value
plus_one = num + 1
#print (plus_one)

#print the hex representation of the integer
print ("\nThe checksum is : ", hex(plus_one))



