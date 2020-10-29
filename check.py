"""
def main():
    print('1. Enter a new pet')
    print('2. Retrieve a pet')
    print('3. Exit')

    while True:
        a=input('which service do you want? : ')
        if a=='1':
            pet()
            pets.append(pet())
            continue
        elif a=='2':
            b=input("which pet? : ")
            if pets.count(b) > 0:
                # you need to find the index so you can use it 
                i=pets.index(b)
                pets[i].display()
                continue
            else:
                print("animal does not exist")
                continue
        else:
            break

main()
"""

"""
while True:
    a=input('which service do you want? : ')
    if a=='1':
        pets.append(pet())
        print(pets)
        continue
    elif a=='2':
        b=input("which pet? : ")
        for i in pets:
            print(i.display())
    else:
        break

"""