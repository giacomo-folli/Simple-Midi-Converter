from music21 import *


def melody_write(file):
    midif = converter.parse(file)  # open midi file
    s = stream.Stream()  # initiate stream obj
    for n in midif.flat.notes:  # convert into notes
        s.append(n)
    return s  # return stream of notes


def main():
    print("Hello, welcome to the midi-to-score converter :)")
    while True:
        print("------------------------------------------------")
        choice = input("Choose action:\n" +
                       "1) To proceed\n" +
                       "0) To quit\n" +
                       "-- Choice: ")
        if choice == "1":
            while True:
                file = input("Enter just the name of the file you want to convert: ")
                i = input("You entered the name " + file + ", you wish to proceed? Y/N -> ")
                if i == "N" or i == "n":
                    continue
                elif i == "Y" or i == "y":
                    print("------------------------------------------------")
                    print("-----Converting " + file + ".mid to score-----")
                    filename = file + ".mid"
                    melody_write(filename).show()
                    break
        elif choice == "0":
            print("Bye Bro B)")
            break
        else:
            print("You entered and unknown action! :( Try again")


main()
