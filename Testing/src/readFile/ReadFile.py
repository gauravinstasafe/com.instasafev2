'''
Created on 18-Dec-2017

@author: Gaurav
'''

with open("C://Users/user/Desktop/testing.txt")as F :
    file = F.readlines()
    print(file)
    file = [a.strip() for a in file]
    test = file[0].split(" ")
    print(test)
    test.append('aaaaa')
    print(test)
    test.insert(6,'test')
    print("ppppp" +"   "+ test[0] +"      "+ "wwwwww" "     "+ test[1] + "ttttttt")
    

    filea = open("C://Users/user/Desktop/testing1.txt","w")

    filea.write("This is a test") 
    filea.write("To add more lines.")
    