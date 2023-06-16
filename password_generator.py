import random
element = "!@#$%^&*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_length = int(input("Masukan banyak password yg diinginkan:"))

password = ""
for i in range(pass_length):
    password += random.choice(element)

print(password)
# print('hello world')