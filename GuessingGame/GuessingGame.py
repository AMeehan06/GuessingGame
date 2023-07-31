def main():
    import random
    print ("Guess the number!")
    n = int(input("Enter the limit:  "))
    answer = random.randint(1, n)
    print("I'm thinking of a number from 1 to " + str(n) + ":  ")
    ask = int(input("Your guess:  "))
    count = 0
    while True:
        count += 1
        if ask > answer:
            print("Too high")
            ask = int(input("Your guess:  "))
        if ask < answer:
            print("Too low")
            ask = int(input("Your guess:  "))
        if ask == answer:
            print("Correct! You guessed it in", count, "tries!")
            restart = (input("Would you like  to play again? (y/n): "))
            if restart == 'y':
                main()
            else:
                print("Bye!")

            break
main()

               



