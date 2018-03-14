#   2018,  Lee MacPherson,  leemacpherson@msn.com

# this program takes a list of hex characters and passes them to
#the function "checksum_generator".  for

import  checksum_generator

# Ask for all of the hex values that will be added.  These values will be put in a list.
# A while-loop will be used to add all of the elements in the list

# make a list to store all of the values that have to be added
hex_list = []
hex_value = 0
        
while hex_value != "":
        hex_value = input ("enter the hex values you need to get 2-s complement for: ")
        print ("hex_value is :", hex_value)
        hex_list.append(hex_value)
        if hex_value == "":
                break
       
print ("the list of hex pairs is : ", hex_list)

# remove the quotation character.  pop([index])removes the element at the specified index and returns that element. If index is not specified, it removes and returns last element from the list.
hex_list.pop()

# pass the list of hex pairs as an argument to the module "checksum_generator"

checksum = checksum_generator.chksum_gen (hex_list)

#indicate that you have had the checksum returned from the module checksum_generator

print ("the 'checksum_generator' module has returned back to 'mrx4000_Commands")

print ("checksum is : ", checksum)
print ("hex_list is : ", hex_list)

#strip off the leading 0x from checksum
checksum_short = checksum[2:4]
print ("checksum is : ", checksum_short)

# append checksum and 03 to the end of the list

hex_list.append(checksum_short)
hex_list.append("03")

print ("after appending checksum and 03, hex_list is : ", hex_list)

#add 19 to the beginning of the list
hex_list.insert(0, 19)
print ("after inserting 19 , hex_list is : ", hex_list)




