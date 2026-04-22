import random


def main():
    print("Khansole Academy")
    current_row=0
    while current_row < 3:
        rand_num_1= random.randint(10, 99) 
        rand_num_2= random.randint(10, 99)
        print(f"What is {rand_num_1} + {rand_num_2}?")
        correct_answer = rand_num_1 + rand_num_2
        answer=int(input("Your answer: "))
        if answer == correct_answer:
            current_row = current_row + 1
            print("Correct!")
            print(f"You've gotten {current_row} correct in a row.")
        else:
            print("Incorrect.")
            print(f"The expected answer is {correct_answer}")
    if current_row == 3:
            print("")
            print("Congratulations! You mastered addition.")   

    
if __name__ == '__main__':
    main()