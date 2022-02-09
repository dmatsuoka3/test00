#!/usr/bin/env python3

all_words = {
     "Name" : "Daigo Matsuoka",
     "Age" : "22",
     "Major" : "Computer Science",
     "Eyes Color" : "Dark Brown"
}

def banner():
    print("\n***************************")
    print("\t1. Search Word")
    print("\t2. Add New Word")
    print("\t3. Update Word")
    print("\t4. Display Entire Dictionary")
    print("\t5. Exit")
    print("*****************************")

def display():
    print("Words in the dictionary\n")
    for key in all_words:
        print("{}: {}".format(key, all_words[key]))

while True:
      try:
          banner()
          choice = int(input("Enter your choice number: "))

          if choice == 1:
             keyInput = input("Enter the Key word to search: ")

             if keyInput in all_words.keys():
                print("{}: {}".format(keyInput, all_words[keyInput]))
             else:
                print("Key Word Not Found. If you wish to add the key word to dictionary press 2")

          elif choice == 2:
             keyInput = input("Enter the Key word to add: ")

             if keyInput in all_words.keys():
                print("{} is already in the dictionary.\nIf you wish to update the meaning, press 3".format(keyInput))
             else:
                addingInput = input("Enter the value of {}: ".format(keyInput))
                all_words[keyInput] = addingInput

          elif choice == 3:
             keyInput = input("Enter the Key word to update: ")

             if keyInput in all_words.keys():
                meaning = input("Enter the meaning of {}: ".format(keyInput))
                all_words[keyInput] = meaning
             else:
                print("{} is not present in dictionary. Press 2 to add".format(keyInput))

          elif choice == 4:
             display()

          elif choice == 5:
             print("Goodbye!")
             break

      except ValueError:
          print("***ERROR***Please choose a number between 1 and 5.")
