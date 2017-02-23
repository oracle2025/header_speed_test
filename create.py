#!/usr/local/env python
import string
import time
import operator
from subprocess import call

# inputfile = "std_include_list.txt"
inputfile = "boost_include_list.txt"
f = open(inputfile, "r")
list_of_headers = [x.strip() for x in f.readlines()]
f.close()

# list_of_headers = [
    # "iostream",
    # "vector",
#     "memory"]

def strip_invalid_chars(inputs):
    delete_table  = string.maketrans(
            string.ascii_lowercase, ' ' * len(string.ascii_lowercase)
    )
    return inputs.translate(None, delete_table)

for header in list_of_headers:
    filename = "output/"+strip_invalid_chars(header) + ".cpp"
    content = "#include <" + header + ">\nint main() {}"
    print filename
    print content
    f = open(filename,"w")
    f.write(content)
    f.close()
    # write to file

result = {}

for header in list_of_headers:
    filename = "output/"+strip_invalid_chars(header) + ".cpp"
    binname = "output/"+strip_invalid_chars(header)
    command = "g++ " + filename + " -o " + binname
    print command
    start_time = time.time()
    # call(["gcc", filename, "-std=c++11", "-o", binname])
    call(["g++", "-I/usr/local/include/", "-c", filename, "-o", filename+".o", "-std=c++11"])
    # duration = "--- %s seconds ---" % (time.time() - start_time)
    duration = (time.time() - start_time)
    result[header] = duration

#sort result by time
sorted_x = sorted(result.items(), key=operator.itemgetter(1))

# for key, value in result.iteritems():
for key, value in sorted_x:
    # duration = "--- %s seconds ---" % (time.time() - start_time)
    print key + ": " + ("--- %s seconds ---" %  value)



