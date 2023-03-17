#Xalan Dames
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(encode_input):
    encoded_list=[]

    for i,num in enumerate(encode_input):
        encoded_list.append(str((int(num)+3)%10))

    print("Your password has been encoded and stored!")

    return(encoded_list)




def main():

    while True:
        menu()
        option=int(input("\nPlease enter an option: "))


        if option==1:
            encode_input = input("Please enter your password to encode:")
            encoded_list=encode(encode_input)
        elif option==3:
            exit(0)






main()
