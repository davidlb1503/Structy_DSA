#Write a function, max_value, that takes in list of numbers as an argument. The function should return the largest number in the list.
#Solve this without using any built-in list methods.
#You can assume that the list is non-empty.

# def max_value(nums):
#   temp = 0
#   first = nums[0]
#   for i in range(len(nums)):
#     if nums[0]<nums[i]:
#       nums[0] = nums[i]
#   return nums[0]

def max_value(nums):
  max_value = float('-inf')
  for i in range(len(nums)):
    if nums[i]>max_value:
      max_value = nums[i]
  return max_value

      
