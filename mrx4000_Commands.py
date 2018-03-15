#   2018,  Lee MacPherson,  leemacpherson@msn.com

# this program takes a list of hex characters and passes them to
#the function "checksum_generator".  for

import  checksum_generator
import codecs

# Ask for all of the hex values that will be added.  These values will be put in a list.
# A while-loop will be used to add all of the elements in the list

# make a list to store all of the values that have to be added
hex_list = []
hex_value = 0
        
while hex_value != "":
        hex_value = input ("enter the MID and Body values: ")
        #print ("hex_value is :", hex_value)
        hex_list.append(hex_value)
        if hex_value == "":
                break
       
#print ("the list of hex pairs is : ", hex_list)

# remove the quotation character.  pop([index])removes the element at the specified index and returns that element. If index is not specified, it removes and returns last element from the list.
hex_list.pop()

# pass the list of hex pairs as an argument to the module "checksum_generator"

checksum = checksum_generator.chksum_gen (hex_list)

#indicate that you have had the checksum returned from the module checksum_generator

print ("the 'checksum_generator' module has returned back to 'mrx4000_Commands")

print ("checksum is : ", checksum)
#print ("hex_list is : ", hex_list)

#strip off the leading 0x from checksum
checksum_short = checksum[2:4]
#print ("checksum is : ", checksum_short)
#print ("checksum[0] is : ", checksum_short[0])
#print ("checksum[1] is : ", checksum_short[1])
#print ("type of checksum_short is ", type (checksum_short))

# assume the two checksum characters are lowercase letters (worse case) and convert both to uppercase with the
# str class method upper( )
checksum_upper_1 = checksum_short[0].upper()
checksum_upper_2 = checksum_short[1].upper()
#print("checksums after they are both run through the uppercase coversion: ", checksum_upper_1, checksum_upper_2)

# find the ascii value of each of the two checksum characters so they can put put in with the other characters
checksum_1 = format(ord(checksum_upper_1), "x")
#print ("checksum_1 is :", checksum_1)
checksum_2 = format(ord(checksum_upper_2), "x")
#print ("checksum_2 is :", checksum_2)


# append checksum and 03 to the end of the list

hex_list.append(checksum_1)
hex_list.append(checksum_2)
hex_list.append("03")

#print ("after appending checksum and 03, hex_list is : ", hex_list)

#add 19 to the beginning of the list, then add the percent % character before the 19
hex_list.insert(0, '19')
#print ("after inserting 19 , hex_list is : ", hex_list)

#finally, use the join() method to join each item in the list into one string with the % character between each one
final_list = "%".join(hex_list)
print (" put a '%' in front of the 19 then copy, paste this string into the AIB-4 table ; ", final_list)




