def main():
    while True:
        print("Choose one you like")
        print("1. Active")
        print("2. Relaxing")
        choice = input("Which one do you choose: Active OR Relaxing holiday: ")
        if choice == '1':
            print("1. Mountains / 2. Forest / 3. Desert")
            a = input("Which option do you choose?(1/2/3): ")
            if a == '1':
                print("You choose to go to Mountains, don't forget to have poles to climb")
                break
            elif a == '2':
                print("Your choice to go to the Forest, please drive a clearence's big enough car")
                break
            elif a == '3':
                print("Your choice to go to the Desert, get yourself a Compas to do not get to confused on your way!")
                break
        elif choice == '2':
            print("1. Beach / 2. SPA / 3. Hotel") 
            a = input("Which option do you choose?(1/2/3): ")
            if a == '1':
                print("You choose to go the Beach, bring yourself an Umbrella, so you don't get burned by sun")
                break
            elif a == '2':
                print("SPA is a great to choice to chillax, just come")
                break
            elif a == '3':
                print("Your choice was a hotel, If you are about to stay longer days, don't forget to bring a suitcase with some clothes")
                break
if __name__ == '__main__':
    main()