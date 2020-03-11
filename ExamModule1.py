# Question No.1
# Create a function called Hashtag that generate hashtag which accepting string separated
# by space as presented in the below with following rules.



# def generate_hashtag(s):
#     z ="#"
#     for i in s.split():
#         z += i.capitalize()

#     if len(z) > 140 or z == '#':
#         print(False)
#     else:
#         print(z)
# generate_hashtag("Hello there how are you doing")
# generate_hashtag("   Hello  world")
# generate_hashtag("")




# Question No.2
# Write a function that accepts a list of 10 integers (between 0 and 9), that returns a string
# of those numbers in the form of a phone number.


# def create_phone_number(n):
#     try:
#         print('({}{}{}) {}{}{}-{}{}{}{}'.format(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9]))
#     except:
#         print(False)  
# create_phone_number([1,2,3,4,5,6,7,8,9,0])
# create_phone_number([1,2,3,4,5,6,7,8,9])             




# Question No.3
# You are given a list of integers. Your task is to sort odd numbers within the list in ascending
# order, and even numbers in descending order but keep all the odds or the evens number in
# the same index group


def sort_odd_even(num):
    idx_odd = []
    val_odd = []
    idx_even = []
    val_even = []
    hasil = [0 for i in range(len(num))]
    for idx, val in enumerate(num):
        if val % 2 != 0:
            idx_odd.append(idx)
            val_odd.append(val)
        else:
            idx_even.append(idx)
            val_even.append(val)
    
    val_odd.sort()
    for i in range(len(val_odd)):
        for j in range(i+1, len(val_odd)):
            if val_odd[i] > val_odd[j]:
                val_odd[i], val_odd[j] = val_odd[j], val_odd[i]
    
    val_even.sort(reverse= True)
    for i in range(len(val_even)):
        for j in range(i+1, len(val_even)):
            if val_even[i] < val_even[j]:
                val_even[i], val_even[j] = val_even[j], val_even[i]

    for idx, val in zip(idx_odd, val_odd):
        hasil[idx] = val
    for idx, val in zip(idx_even, val_even):
        hasil[idx] = val
    print(hasil)    

sort_odd_even([5,3,2,8,1,4])

           



# Question No.4
# Create a function hollowTriangle(height) that returns a hollow triangle of the correct
# height or level.


# def hollow_triangle(n):
#     if n == 1:
#         print("#")
#         return False

#     atas = ["_" * (n - 1) + "#" + "_" * (n - 1)]
#     bawah = ["#" * ((2 * n) - 1)]
#     mid = []
#     for i in range(n - 2, 0, -1):
#         mid.append(("_" * i) + "#" + ("_" * ((2 * n) - (2 * i) - 3)) + "#" + ("_" * i))
    
#     print(atas[0])

#     for i in mid:
#         print(i)

#     print(bawah[0])  
    
# for i in range(1, 7):
#     hollow_triangle(i)        