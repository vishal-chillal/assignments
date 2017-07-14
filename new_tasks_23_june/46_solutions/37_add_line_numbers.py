# 37.Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n (where n is the number of lines in the file).
def create_file_and_copy_text(file_name, file_text):
    try:
        with open(file_name,"w+") as fp:
            line_num = 0
            for line in file_text:
                line_num += 1
                fp.write(str(line_num) + " " + line + "\n")
    except Exception as e:
        print e

def get_data(file_name):
    file_data = None
    try:
        with open(file_name, "r") as fp:
            file_data = fp.read().split('\n')
    except Exception as e:
        print e

    return file_data

if __name__ == "__main__":
    # sorce_name = raw_input("enter source file name: ")
    source_name = "./semordnip_inp.txt"
    destination_name = raw_input("enter destination file name: ")
    file_data = get_data(source_name)
    create_file_and_copy_text(destination_name, file_data)
