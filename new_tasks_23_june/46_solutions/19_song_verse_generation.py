# Your task here is write a Python program capable of generating all the verses of the song.
def generate_verses():
    line1 = " bottles of beer on the wall,"
    line2 = " bottles of beer. Take one down, pass it around,"
    line3 = " bottles of beer on the wall.\n"
    song  = ""
    for i in xrange(100,0,-1):
        song += str(i-1) + line1
        song += str(i-1) + line2
        song += str(i-2) + line3

if __name__ == "__main__":
    generate_verses()
