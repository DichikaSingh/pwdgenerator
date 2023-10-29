#Task 2( PASSWORD GENERATOR )
import random as ra
def create():
    print("Welcome to Password generator")
    characters= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*"
    password_lenght=int(input(f"Enter your password lenght:  "))
    password=""
    for a in range(password_lenght):
        password+=ra.choice(characters)
    print(password)    

    print("I hope this Password generator helps you to bulid a strongest password.")
