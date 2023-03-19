###ROADMAP:
###-Export to different modes (E.g: List of songs (oneliner))
###-Add UI
###########
import os
import configparser
import re #regex

actualfolder = os.getcwd()

#initiate parser
config = configparser.ConfigParser()
config.read('inventory.ini')

# Check if the file exists
if not os.path.exists('inventory.ini'):
    # Create a new file if it doesn't exist and add the first section.
    with open('inventory.ini', 'w') as f:
        print("I didn't find the inventory. Creating a new one under: "+actualfolder)
        artist = input("Enter artist name: ") or 'N/A'
        song_title = input("Enter song title: ") or 'N/A'
        remix = input("Enter remix name: ") or 'N/A'
        mashup = input("Is this a mashup? ") or 'N/A'
        genre = input("Insert genre: ") or 'N/A'
        released = input("Is this song released? ") or 'N/A'
        f.write('[Song1]\n')
        f.write(f'Artist = {artist}\n') 
        f.write(f'Title = {song_title}\n')
        f.write(f'Remix = {remix}\n')
        f.write(f'Mashup = {mashup}\n')
        f.write(f'Genre = {genre}\n')
        f.write(f'Released = {released}\n')

# Initiate parser
config = configparser.ConfigParser()
config.read('inventory.ini')

# Define sections in the INI file
sections = config.sections()

def show_inventory():
        # Code to show inventory goes here
        # Loop through each section and extract the data
        for section in sections:
            artist = config.get(section, 'Artist')
            song_title = config.get(section, 'Title')
            remix = config.get(section, 'Remix')
            mashup = config.get(section, 'Mashup')
            genre = config.get(section, 'Genre')
            released = config.get(section, 'Released')

            # Print the data for each section
            print(f'{section}')
            print(f'Artist: {artist}')
            print(f'Title: {song_title}')
            print(f'Remix: {remix}')
            print(f'Mashup: {mashup}')
            print(f'Genre: {genre}')
            print(f'Released: {released}')
            print()

def add_entry():
    # Get the last section in the INI file and determine the new section name
    last_section = config.sections()[-1]
    last_number = int(last_section.split('Song')[1])
    new_section_number = last_number + 1
    new_section = 'Song' + str(new_section_number)

    # Create a new section for the new entry
    config[new_section] = {}

    # Set the values for the new entry
    config[new_section]['Artist'] = input("Enter the (original) artist name: ") or 'N/A'
    config[new_section]['Title'] = input("Enter the song title: ") or 'N/A'
    config[new_section]['Remix'] = input("Is this a remix? ") or 'N/A'
    config[new_section]['Mashup'] = input("Is this a mashup? ") or 'N/A'
    config[new_section]['Genre'] = input("Enter the genre: ") or 'N/A'
    config[new_section]['Released'] = input("Is the song released? (yes/no) ") or 'N/A'

    # Write the changes back to the INI file
    with open('inventory.ini', 'w') as configfile:
        config.write(configfile)

def remove_entry():
        # Code to remove entry goes here
    # Print the sections with their corresponding index to the user
    print('Sections in the INI file:')
    for i, section in enumerate(sections):
        print(f'{i+1}. {section}')
        for key, value in config[section].items():
            if value != "N/A":
                print(f'\t{key}: {value}')

    # Ask the user to enter an integer to delete the corresponding section
    selection = input('Enter the number of the section to delete: ')

    # Check if the selection is within range
    if selection < 1 or selection > len(sections):
        print('Invalid selection. Please enter a number within the range of sections.')
        exit()

    # Get the section name based on the user input
    section_to_delete = sections[selection - 1]

    # Print the values for the user to confirm
    print(f'Values for {section_to_delete}:')
    for key, value in config[section_to_delete].items():
        print(f'{key}: {value}')

    # Ask the user to confirm the deletion
    #confirmation = input('Are you sure you want to delete this section? (Y/n) ')
    confirmation = input('Are you sure you want to delete this section? (Y*/n) ') or 'y'

    if confirmation.lower() == 'y':
        # If the user confirms, delete the section and write the changes back to the INI file
        config.remove_section(section_to_delete)
        with open('inventory.ini', 'w') as configfile:
            config.write(configfile)
        print(f'{section_to_delete} has been deleted.')
    else:
        # If the user does not confirm, do not delete the section
        print(f'{section_to_delete} has not been deleted.')

def find_entries_by_genre():
    genre_name = input("Enter the name of the genre: ")

    entries = []
    for section in config.sections():
        if 'genre' in config[section]:
            genre = config[section]['genre']
            if re.search(genre_name.lower(), genre.lower()):
                entries.append(dict(config[section]))

    # print the entries found
    if entries:
        print("Entries found for genre: ", genre_name)
        for i, entry in enumerate(entries):
            print(f"Entry {i + 1}:")
            for key, value in entry.items():
                print(f"{key}: {value}")
            print("")
    else:
        print("No entries found for genre: ", genre_name)

def exit_program():
        print("Exiting the program...")
        quit()

    # Dictionary of functions
menu_options = {
        "1": show_inventory,
        "2": add_entry,
        "3": remove_entry,
        "4": find_entries_by_genre,
        "5": exit_program
    }

# Print the menu
#Print menu:
print("1- Show inventory")
print("2- Add entry to inventory")
print("3- Delete entry from inventory")
print("4- Find entries by genre")
print("5- Exit")

# Ask the user for input
choice = input("Please enter your choice: ")

# Call the appropriate function based on user input
menu_options.get(choice, lambda: print("Invalid choice. Please try again."))()