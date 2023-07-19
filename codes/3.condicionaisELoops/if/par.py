num= int(input("Type the number that you need to study"));
text= " "

if(num%2==0):
    text= "even.";
else:
    text= "odd.";
    
print("The number is {}".format(text));