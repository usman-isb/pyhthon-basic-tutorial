# color = input("Enter a color")
# plural_noun = input("Enter a plural noun")
# celebrity = input("Enter a celebrity")
#
# print("Roses are "+color)
# print (plural_noun+ " are blue")
# print ("I love "+celebrity)
#

# lucky_numbers=[2,5,9,10,4]
# friends=["usman","zoraiz","gomarkho","solarforschools"]
# friends.extend(lucky_numbers) # add to list together
# # append other item to list
# friends.append("Google")
# #insert on specific index
# friends.insert(2,"Good")
# #Remove value form list
# friends.remove("Good")
#
# #find in list
# print(friends.index("Google"))
# friends.clear()
# print(friends)

# functions
# def hello_world(a, b):
#     return a+b
# print (hello_world(1,2))

def max_num(num, num2, num3):
    if num>=num2 and num>num3:
        return  num
    elif num2>=num and num2>num3:
        return  num2
    else:
        return  num3

print(max_num(1, 2,3))