from random import randint
import sys

# List item extractor
# By Amosnimos
# 11 septembre 2024
# A program that print the largest int in a list

# Find largest item in a list of int
def largest_item():
    # Init empty array for the notes
    notes = []
    # Load values from arguments if provided
    if (sys.argv and len(sys.argv) > 1):
            # Convert convert the first argument string to an array if it contains "," character.
            # If is a sort of list
            if "," in sys.argv[1]:
                notes=str(sys.argv[1]).strip("[](){}abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRS!@#$%^&*()_+").split(',')
            else:
                # Take every argument as a list item
                notes=sys.argv[1:]

    # Init variables
    max_note=0
    if notes == []:
        # If no arguments are provided create an array of random value
        array_size=20 # Default array size
        notes=[None]*array_size # Create an array of None of size array_size
        max_value=100 # 
        array_start=0
        
        # From 0 to Array_size append a random note to the notes array.
        for note_index in range(array_start,array_size):
            notes[note_index]=randint(array_start,max_value)
            # Display array of notes in the terminal
        print("NOTES: "+str(notes))
    else:
        # If the notes array arlready exist use it's size as array_size 
        array_size=len(notes)

    # Look for largest note in the notes array
    for note in notes:
        # If note is a valid number compare it's value to max_note
        try:
            if type(int(note[0]))==int:
                if (int(note[0]) > int(max_note)):
                    max_note=note[0]
            else:
                print(type(note))
        except:
            # If the note is not a valid number ignore it.
            continue
            #print("Skipping ("+str(note)+")")

    # Display the largest note
    return max_note

print(largest_item())
