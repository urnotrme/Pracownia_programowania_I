pin='0805'
g=input("Enter the PIN code: ")
x=1
if pin==g:
    print("Correct!")
elif pin!=g:
    print("Incorrect...")
    g=input("Enter the PIN code: ")
    x+=1
    if x==3:
        print("Sorry, your payment card has been blocked.")

