import json

array = list(range(1, 10000))
start = 0
index = 20
long = 100

with open("output.json", "w") as file:
    file.write("[")
    for i in range(len(array) // index - 1):

        array_new = array[start : start + long]
        start += index
        print("New: ", array_new)
        print("i: ", i)

        # write array_new to JSON file
        json.dump(array_new, file)
        file.write(",\n")

    # remove the last "," and add "]" to the end of the file
    file.seek(file.tell() - 2, 0)
    file.write("]")






