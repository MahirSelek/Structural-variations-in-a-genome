#!/ usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("Syntax: " + sys.argv[0] + " file.sam genomelength")
    exit()

genome_length = int(sys.argv[2]) 
genome_change = [0]*genome_length # genome change is a list of integers all set to zero

sam_file = open(sys.argv[1]) # open sam file
for line in sam_file: # read each line into the variable "line"
    if line[0] != '@': # do the block below only if line doesn't start with @
        continue
        
    fields = line.split("\t")   # make list of tab-separated fields
    try: 
        multiple = fields[16] 
    except IndexError:
         continue 
    mul = multiple.split(";") 
    
    for i in range(len(mul) - 1): 
        array = mul[i].split(",")
        genome_change[abs(int(array[1]))] += 1 
        genome_change[abs(int(array[1])) + 100] -= 1         

sam_file.close()

print("fixedStep chrom=genome start=1 step=1 span=1") # print track as a wiggle file
current_coverage = 0 

for position in range(genome_length): # cicle over all positions of the genome
    current_coverage = current_coverage + genome_change[position] 
    print(current_coverage)
