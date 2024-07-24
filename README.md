# Binary-Multiplication-Algorithms
This project implements binary multiplication using two different algorithms: Add & Shift and Booth's Algorithm. The code is written in Python and includes both signed and unsigned multiplication.

# Project Overview
The project is designed to perform binary multiplication using two different methods:

1. Add & Shift Multiplication
2. Booth's Algorithm

Both methods support signed and unsigned binary multiplication. The program reads input from a text file (in.txt) and writes the output to another text file (out.txt).
# Files
1. main.py: Contains the implementation of the binary multiplication algorithms and the logic to read input and write output.

2. in.txt: The input file containing the parameters for the multiplication tasks.

3. out.txt: The output file containing the results of the multiplication tasks.

# Input File Format (in.txt)
The input file should contain the following data:

1. The first line contains an integer n, the number of multiplication tasks.
2. For each task, there are five lines:
    m: Algorithm type (0 for Add & Shift, 1 for Booth's Algorithm)

    b: Bit length of the operands
  
    s: Signedness (0 for unsigned, 1 for signed)
  
    A: First operand in decimal
  
    B: Second operand in decimal
  

# Example
4

1

6

0

11

13

1

6

1

-5

-3

0

4

0

11

13

0

4

1

-5

-3

# Output File Format (out.txt)
The output file contains the results of each multiplication task, including intermediate steps and final results in both binary and decimal formats.

# Example

------------------------------------------

out-0

unsigned add & shift multiplication

A=11=1011, B=13=1101

~~~~~~~~~~~~~~~~~~~~

(0, ) M=0000|1101

~~~~~~~~~~~~~~~~~~~~

(1,+) M=1011|1101

(1,>) M=01011|110

~~~~~~~~~~~~~~~~~~~~

(2, ) M=01011|110

(2,>) M=001011|11

~~~~~~~~~~~~~~~~~~~~

(3,+) M=110111|11

(3,>) M=0110111|1

~~~~~~~~~~~~~~~~~~~~

(4,+) M=0001111|1

(4,>) M=10001111

~~~~~~~~~~~~~~~~~~~~

M=AxB=143

------------------------------------------

out-1

signed add & shift multiplication

A=-5=1011, B=-3=1101

~~~~~~~~~~~~~~~~~~~~

(0, ) M=0000|1101

~~~~~~~~~~~~~~~~~~~~

(1,+) M=1011|1101

(1,>) M=11011|110

~~~~~~~~~~~~~~~~~~~~

(2, ) M=11011|110

(2,>) M=111011|11

~~~~~~~~~~~~~~~~~~~~

(3,+) M=100111|11

(3,>) M=1100111|1

~~~~~~~~~~~~~~~~~~~~

(4,-) M=0001111|1

(4,>) M=00001111

~~~~~~~~~~~~~~~~~~~~

M=AxB=+15

# Running the Code
1. Ensure you have Python installed.
2. Place the in.txt file in the same directory as main.py.
3. Run the script using the command: python main.py
4. Check the out.txt file for the results.

# Functions

# Main Functions
add_shift(b, s, A, B): Performs unsigned or signed multiplication using the Add & Shift method.

booth_algorithm(b, s, A, B): Performs unsigned or signed multiplication using Booth's Algorithm.

# Helper Functions
binary_addition_to_find_carry(x, y, bits): Finds the carry bit in binary addition.

unsigned_process(b, M, A): Processes unsigned multiplication.

signed_process(b, M, A, neg_A): Processes signed multiplication.

to_twos_complement(value, bits): Converts a value to its two's complement binary representation.

arithmetic_shift_right(M, shifts): Performs arithmetic right shift.

binary_addition(x, y, bits): Adds two binary numbers.

RedirectStdout(new_stdout): Redirects the standard output to a file.
