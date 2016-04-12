import sys
# argv[1]: input file's path
# argv[2]: output file's path
with open(sys.argv[2], mode='a') as output_file:
    for line in open(sys.argv[1], mode='r'):
        # append into output_file
        output_file.write(line)
        
    

