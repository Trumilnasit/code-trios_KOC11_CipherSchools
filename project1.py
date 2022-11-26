# Project to make a currency Generator
currency={"USD":81,"EUR":84,"INR":1,"GBP":98,"AUD":55,"CAD":61,"SGD":59.36,"CHF":86,"MYR":18.23,"JPY":0.58,"CNY":11.38,"AED":22.23,} # Add more currency here
def convert(c1,a,c2):
    if(c2=="INR"):
        print("The Currency After Converting into %s is"%c2,(amount*currency[c1]))
    elif(c1=="INR"):
        print("The Currency After Converting into %s is"%c2,(amount/currency[c2]))
    else:    
        print("The Currency After Converting into %s is"%c2,(amount*(currency[c1]/currency[c2])))

print(" ---------------------- ")
print("|  Currency Converter  |")
print(" ---------------------- ")
for i in currency.keys():
    print(i)
c1=input("Enter The Currency(case sensitive): ") #The Currency given
amount=eval(input("Enter The Amount: ")) # The amount in the given currency
c2=input("Enter The Currency you want to convert to(case sensitive): ") # The currency you want to covert the amountUSD
convert(c1,amount,c2)