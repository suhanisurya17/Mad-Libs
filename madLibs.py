print("Welcome to Mad Libs!")
print("In this program, you will be able to have fun and try out different scenarios "
      "that will create funny stories that are sure to make you laugh!")
print("Choose one of the following scenarios and type the number of the scenario you would like to choose.")
print("1: Mysterious Adventure Story")
print("2: The Culinary Contest")
print("3: The Time Traveler's Dilemma")

def scenario1():
    print("Welcome! This is the Mysterious Adventure Story")
    fitb1 = input("give me an adjective: ")
    fitb2 = input("give me a noun: ")
    fitb3 = input("give me an adjective: ")
    fitb4 = input("give me a noun: ")
    fitb5 = input("give me an adjective: ")
    fitb6 = input("give me a noun: ")
    fitb7 = input("give me a plural noun: ")
    fitb8 = input("give me an animal: ")
    fitb9 = input("give me an article of clothing: ")
    fitb10 = input("give me a body part: ")
    fitb11 = input("give me a verb: ")
    fitb12 = input("give me an adjective: ")
    fitb13 = input("give me a noun: ")
    fitb14 = input("give me a famous person: ")
    fitb15 = input("give me a noun: ")
    print("Once upon a time, in a(n) " + fitb1 + "forest, there lived a curious {fitb2}."
          " This {fitb3} creature loved exploring, and one day, it stumbled upon a magical {fitb4}."
          " The {fitb5} {fitb2} decided to enter the {fitb4} and found a world filled with {fitb6}. "
          "The {fitb7} in this land were friendly and led the {fitb2} to meet a wise {fitb8}. "
          "The {fitb8} offered a magical {fitb9} that granted the {fitb2}'s {fitb10} the power to {fitb11}. "
          "With this newfound ability, the {fitb2} went on many {fitb12} adventures and eventually became a legendary {fitb13}. "
          "Some say this {fitb2} was as famous as {fitb14} and had a heart as big as a(n) {fitb15}.")
def scenario2():
    print("Welcome! This is the Culinary Contest Story")
    fitb1 = input("give me an adjective: ")
    fitb2 = input("give me a noun: ")
    fitb3 = input("give me an adjective: ")
    fitb4 = input("give me a noun: ")
    fitb5 = input("give me an adjective: ")
    fitb6 = input("give me a noun: ")
    fitb7 = input("give me a plural noun: ")
    fitb8 = input("give me an animal: ")
    fitb9 = input("give me an article of clothing: ")
    fitb10 = input("give me a body part: ")
    fitb11 = input("give me a verb: ")
    fitb12 = input("give me an adjective: ")
    fitb13 = input("give me a noun: ")
    fitb14 = input("give me a famous person: ")
    fitb15 = input("give me a noun: ")

def scenario3():
    print("Welcome! This is the Time Traveler's Dilemma")
    fitb1 = input("give me an adjective: ")
    fitb2 = input("give me a noun: ")
    fitb3 = input("give me an adjective: ")
    fitb4 = input("give me a noun: ")
    fitb5 = input("give me an adjective: ")
    fitb6 = input("give me a noun: ")
    fitb7 = input("give me a plural noun: ")
    fitb8 = input("give me an animal: ")
    fitb9 = input("give me an article of clothing: ")
    fitb10 = input("give me a body part: ")
    fitb11 = input("give me a verb: ")
    fitb12 = input("give me an adjective: ")
    fitb13 = input("give me a noun: ")
    fitb14 = input("give me a famous person: ")
    fitb15 = input("give me a noun: ")



integer_choice = input("Which scenario have you chosen? ")

while integer_choice not in ['1', '2', '3']:
    integer_choice = input("Invalid choice! Please try again: ")

if integer_choice == '1':
    scenario1()
elif integer_choice == '2':
    scenario2()
elif integer_choice == '3':
    scenario3()

