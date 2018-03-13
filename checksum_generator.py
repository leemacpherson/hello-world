#   2018,  Lee MacPherson,  leemacpherson@msn.com

# this program accepts a list of hex characters from the module "mrx4000_commands"
# "checksum_generator" passes back a single two-character checksum to "mrx4000_commands"
# one list of variable length is passed to this function and this function returns on hex value back to the calling function


#import random

def chksum_gen (hex_lst):

#declare the list that will hold the decimal equivalent of all of the hex values
    dec_list = []
    i= 0

    while i  < (len(hex_lst)-1):
        dec_list[i] = int(hex_lst[i], 16)
        #dec_value = int(hex_value, 16)

    print ("the list of decimal equivalents is : ", dec_list)

# calculate the sum of all of the elements, then print the decimal value

dec_sum = sum(dec_list)
print("the sum is: ", dec_sum)

# convert the decimal value to a binary value
bin_sum = bin(decimal_sum)
print("the binary value is : ", bin_sum)
  
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



