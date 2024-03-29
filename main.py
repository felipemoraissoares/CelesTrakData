## Project CEI SSCS
## Author: Felipe de Morais Soares 
##
## Simple Python project to obtain data of objects in space orbit from http://celestrak.com/
## The TLE data will be saved in a csv file according to insert NoradID
## The information is acquired at http://celestrak.com/NORAD/documentation/gp-data-formats.php
## The results are converted from TLE's format to CSV but preserved the line1 and line2 strings
## The Query informations and outputs files can be changed in args.py
##

from tlereader import tlereader

if __name__ == '__main__':

    print("Type A for all Active Satellites or enter with NoradID...")
    print("")

    valid_id = False
    while not valid_id:
        usr_input = input("Enter the desired option: ")
        if usr_input.lower() == "a":
            tlereader("all")
            valid_id = True
        else:
            try:
                int(usr_input)
                tlereader(usr_input)
                valid_id = True
            except ValueError:
                print("Please type a valid command!")

    print("End of Process!")
