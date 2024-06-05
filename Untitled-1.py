# #python3tests
# #massive

# nums = [5,7,-4,5.45,True,6]
# nums[0] = 34.34
# # print(nums[3]) 

# nums2 =[5,7,3,[5,"Text", True]]
# # print(nums2[-2])

# nums.append(45)
# nums.insert(1,False) #konkretno vstavit po index
# #nums.extend(nums2) #dobavlyaet spiski k spiskam, de to tak
# nums.sort()
# nums.reverse()
# #nums.pop() # delete last added
# nums.remove(34.34)
# #nums.clear()

# print(nums)
# print(nums.count(6))
# print(len(nums))



# # nums.insert(1, False)
# # 
# # nums.sort()

# # print(nums)
# # nums.reverse() #pereveorechivaet spisok v print()
# # nums.pop() #kill last is the spisok
# # nums.remove()
# # nums.count()

# # print(len(nums)) #show you lenth of the file 


##################################################################
                    #STORAGES AND MASSIVES#
##################################################################

# nums = [5, 3, 2, 6.5]

# for el in nums:
#     res = el ** 2
#     print(res)
# print(nums)

############practice#############

user_count_hobby = input("Enter number for test: ")

i = 0
hobby = []
while i < user_count_hobby:
    text = "Enter hobby" + i +": "
    hobby.append(input(text))

    i +=1
print(hobby)