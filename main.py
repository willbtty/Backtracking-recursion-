from Exec import Exec


try:
    floodFile = input("Please provide the name of the input file: ")
    Floodsim = Exec(floodFile)
    Floodsim.readFile()
except FileNotFoundError:
    exit("No file found with that name exiting program")