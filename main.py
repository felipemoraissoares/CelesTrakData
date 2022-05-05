##
## Simple Python projetct to obtain data of objects in space orbit from http://celestrak.com/
## The TLE data will be saved in a csv file according to insert NoradID
## The information is acquired at http://celestrak.com/NORAD/documentation/gp-data-formats.php
## The results are converted from TLE's format to CSV but preserved the line1 and line2 strings
## The Query informations and outputs files can be changed in args.py
##

from tlereader import tlereader

if __name__ == '__main__':

    valid_id = False

    while not valid_id:
        noradid = input("Set the object NORAD ID: ")

        try:
            int(noradid)
            tlereader(noradid)
            valid_id = True

        except ValueError:
            print("Please insert a valid NoradID!")

    print("End of Process!")
