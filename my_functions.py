from random import randint
import sys

# Find largest item in a list of int
def largest_item():
    # Init empty array for the notes
    notes = []
    # Load values from arguments if provided
    if (sys.argv and len(sys.argv) > 1):
            # Convert convert the first argument string to an array if it contains "," character.
            if "," in sys.argv[1]:
                notes=sys.argv[1].strip("[]").split(',')
            else:
                notes=sys.argv[1:]

    # Init variables
    max_note=0
    if notes == []:
        # If no arguments are provided create an array of random value
        array_size=20
        notes=[None]*array_size # Create an array of None of size array_size
        max_value=100
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
            if type(int(note))==int:
                if (int(note) > int(max_note)):
                    max_note=note
            else:
                print(type(note))
        except:
            # If the note is not a valid number ignore it.
            continue
            #print("Skipping ("+str(note)+")")

    # Display the largest note
    return max_note

print(largest_item())