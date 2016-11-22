# secretSantaHelper
Creates a Secret Santa chain that ensures no members have each other or other members from same group

Overview:
This program pulls data from 'input.txt' consisting of any number of people placed into
any number of groups and writes to 'output.txt' a single chain of names where no person
gives to another person inside the same group as them. 

This program will fail (and write out an error) if one group contains more than 50% of the
total number of people in the file. This configuration does not have a solution to satisfy
the above.

The program may be rerun to provide different configurations for the Secret Santa, although
the ordering is not completely random.

input.txt:
Format the file as indicated by the example input.txt file. Grouping names must start with
a '-' and may follow with any identifier. Place one name per line. No final new line is
required after the last entry

output.txt:
A Secret Santa chain is written to the output.txt file in the format shown in the example
file. An error will be printed if there is no configuration is possible given the inputs.
