#Importing sha512_crypt from passlib library to use it for hashing
from passlib.hash import sha512_crypt

#Defining a function that takes the password and the salt and
#1) Produce the hash of the password
#2) Compares it to the hash in the shadow file

def passCrack(line,salt,hash):
    
    #hash the password + salt using SHA-512
    pswd_hash= sha512_crypt.using(salt=salt, rounds=5000).hash(line)
    #the hash we found in the shadow file
    pswd_user= "$6$" + salt +"$" + hash

    #3) If it's a match, it prints out the password and returns true
    if pswd_hash== pswd_user:
        print("The password is " + line)
        return True

    #4) If not, it returns false and the loop continues
    else: 
        return False

#Open the text file containing our passwords
with open(r"E:\Uni\Level 4\Cyber Security\Lab 03\100k-most-used-passwords-NIST.txt", errors="ignore") as file:
    #Makes a list of passwords by looping through the file
    lines=[line.rstrip() for line in file]
    
    #ask user to enter the salt and the hash found in the shadow file
    salt= input("Please Enter the salt: ")
    hash= input("Please Enter the hash: ")

    #Loop through the list to try one password at a time
    for line in lines:
        #pass the password and the salt to the function and check whether it mathches.
        #if it does, break the loop
        if passCrack(line,salt,hash) == True:
            break
