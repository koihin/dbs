# dbs

Program name is dbscode2.py. Ran under both Python version 3.84 and 3.97  on Mac OS


Instructions

run dbscode2.py from the command line by invoking Python followed by program, example: 

python dbscode2.py

dbscode2.py takes only 2 optional arguments, an input file name and an output file name,the first argument is the input file, the second is the output file, if you wish to specify the output file, specifying the input file is mandatory.

example:

python dbscode2.py input2.txt  # input2.txt is the input file.

python dbscode2.py input2.txt output2.txt # output2.txt is the output file

If supplied without arguments, the default input file is dbsinputfile.txt and the output file is dbsoutput.txt

The output file will capture the required output. Print statements are only for verification/debugging. 

Notes on program:

1. The message body will only consist of 0s, 1s and newlines. Any other lines are treated as a header file

2. the largest key length is 7 'bits' (0s and 1s stored as a string)

3. we assume the message body may not be well formatted, any key not found is ignored. the rest of the msg is decoded.

4. dbsinputfile.txt is based on the sample input provided by DBS. However the message body of the second msg is structured in such a way it will not give the expected output. I have modified the input data to give the expected output, however you can still run the original input data by running inputorig.txt.

5. inputfile2.txt allows you to test that key lengths of 7 work