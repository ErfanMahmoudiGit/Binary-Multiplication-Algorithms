def binary_addition_to_find_carry(x, y, bits):
    result = int(x, 2) + int(y, 2)
    carry = 0
    if result >= (1 << bits):
        carry = 1
    return carry

def add_shift(b, s, A, B):
    A_bin = format(A, f'0{b}b')
    B_bin = format(B, f'0{b}b')
    neg_A = to_twos_complement(-A, b)
    M = '0' * (b) + B_bin
    
    if s == 0:
        print ("unsigned add & shift multiplication")
        print ("A=", A, "=", A_bin, ", B=", B, "=", B_bin)
        print ("~~~~~~~~~~~~~~~~~~~~")
        print ('(0, ) M=',M)
        print ("~~~~~~~~~~~~~~~~~~~~")
        result_unsigned = unsigned_process(b, M, A_bin)
        return result_unsigned
    elif s == 1:
        A_bin = to_twos_complement(A, b)
        B_bin = to_twos_complement(B, b)
        M = '0' * (b) + B_bin
        print ("signed add & shift multiplication")
        print ("A=", A, "=", A_bin, ", B=", B, "=", B_bin)
        print ("~~~~~~~~~~~~~~~~~~~~")
        print ('(0, ) M=',M)
        print ("~~~~~~~~~~~~~~~~~~~~")
        result_signed = signed_process(b, M, A_bin, neg_A)
        return result_signed
    
def unsigned_process(b, M, A):
    # Helper function to perform right shift with carry
    def logical_right_shift_with_carry(M, carry):
        M = str(carry) + M[:-1]
        return M

    for y in range(int(b)):
        if M[-1] == '0':
            M = logical_right_shift_with_carry(M, 0)
            print ('(',y+1, ',>) M=', M)
            print ("~~~~~~~~~~~~~~~~~~~~")
        else:
            carry = binary_addition_to_find_carry(M[:b], A, b)
            M = binary_addition(M[:b], A, b) + M[b:]
            print ('(',y+1, ',+) M=', M)
            M = logical_right_shift_with_carry(M, carry)
            print ('(',y+1, ',>) M=', M)
            print ("~~~~~~~~~~~~~~~~~~~~")
    return M

def signed_process(b, M, A, neg_A):
    def arithmetic_right_shift_with_carry(M, carry, overflow):
        if overflow == '1':
            M = str(carry) + M[:-1]
        else:
            M = M[0] + M[:-1]
        return M
    
    for y in range(int(b-1)):
        overflow = 0
        if M[-1] == '0':
            M = arithmetic_right_shift_with_carry(M, 0, 0)
            print ('(',y+1, ',>) M=', M)
            print ("~~~~~~~~~~~~~~~~~~~~")
        else:
            carry = binary_addition_to_find_carry(M[:b], A, b)
            if int(M[0]) ^ int(A[0]) == 0: # if xor of the msb's of M and A is 0, means they are both positive or both negative.
                M = binary_addition(M[:b], A, b) + M[b:]
                print ('(',y+1, ',+) M=', M)
                if M[0] != A[0]: # if the result which is now stored in M, has diffrent sign, we have overflow.
                    overflow = 1
            else:
                M = binary_addition(M[:b], A, b) + M[b:]
                print ('(',y+1, ',+) M=', M)
                
            M = arithmetic_right_shift_with_carry(M, carry, overflow)
            print ('(',y+1, ',>) M=', M)
            print ("~~~~~~~~~~~~~~~~~~~~")
            
    overflow = 0
    # Final step
    if M[-1] == '1':
        carry = binary_addition_to_find_carry(M[:b], neg_A, b)
        #### calculate overflow like above:
        if int(M[0]) ^ int(A[0]) == 0: # if xor of the msb's of M and A is 0, means they are both positive or both negative.
            M = binary_addition(M[:b], neg_A, b) + M[b:]
            print ('(',y+2, ',-) M=', M)
            if M[0] != A[0]: # if the result which is now stored in M, has diffrent sign, we have overflow.
                overflow = 1
        else:
            M = binary_addition(M[:b], neg_A, b) + M[b:]
            print ('(',y+2, ',-) M=', M)
            
        M = arithmetic_right_shift_with_carry(M, carry, overflow)
        print ('(',y+2, ',>) M=', M)
        print ("~~~~~~~~~~~~~~~~~~~~")
    else:
        M = arithmetic_right_shift_with_carry(M, 0, 0)
        print ('(',y+1, ',>) M=', M)
        print ("~~~~~~~~~~~~~~~~~~~~")
            
    return M
#######################################################################################################################
def to_twos_complement(value, bits):
    if value < 0:
        value = (1 << bits) + value
    return format(value, f'0{bits}b')

def arithmetic_shift_right(M, shifts):
    for _ in range(shifts):
        M = M[0] + M[:-1]
    return M

def binary_addition(x, y, bits):
    result = int(x, 2) + int(y, 2)
    if result >= (1 << bits):
        result -= (1 << bits)
    return format(result, f'0{bits}b')

def booth_algorithm(b, s, A, B):
    if s == 1:
        print ("signed booth multiplication")
    elif s == 0:
        print ("unsigned booth multiplication")
        
    A_bits = b + 1 

    # Create A in binary format
    if s == 1:
        A_bin = to_twos_complement(A, A_bits)
        B_bin = to_twos_complement(B, b)
    else:
        A_bin = format(A, f'0{A_bits}b')
        B_bin = format(B, f'0{b}b')

    # Initialize M with B and extend with zero bits
    M = '0' * (b + 1) + B_bin + '0'

    A_bin_extended = '0' * (A_bits - len(A_bin)) + A_bin
    neg_A_bin_extended = to_twos_complement(-A, A_bits)
    A_bin_extended_2 = to_twos_complement(2 * A, A_bits)
    neg_A_bin_extended_2 = to_twos_complement(-2 * A, A_bits+1)
    
    print ("A=", A, "=", A_bin, ", B=", B, "=", B_bin)
    print ("~~~~~~~~~~~~~~~~~~~~")
    print ('(0, ) M=',M)
    print ("~~~~~~~~~~~~~~~~~~~~")
    for y in range(int (b/2)):
        last_three_bits = M[-3:]
        if last_three_bits == '000' or last_three_bits == '111':
            M = arithmetic_shift_right(M, 2)
            print ('(',y+1, ',>) M=', M)
            print ("~~~~~~~~~~~~~~~~~~~~")
            
        elif last_three_bits == '001' or last_three_bits == '010':
            M = binary_addition(M[:A_bits], A_bin_extended, A_bits) + M[A_bits:]
            print ('(',y+1, ',+) M=', M)
            M = arithmetic_shift_right(M, 2)
            print ('(',y+1, ',>) M=', M)
            print ("~~~~~~~~~~~~~~~~~~~~")
            
        elif last_three_bits == '011':
            M = binary_addition(M[:A_bits], A_bin_extended_2, A_bits) + M[A_bits:]
            print ('(',y+1, ',+) M=', M)
            M = arithmetic_shift_right(M, 2)
            print ('(',y+1, ',>) M=', M)
            print ("~~~~~~~~~~~~~~~~~~~~")
            
        elif last_three_bits == '100':
            M = binary_addition(M[:A_bits], neg_A_bin_extended_2, A_bits) + M[A_bits:]
            print ('(',y+1, ',+) M=', M)
            M = arithmetic_shift_right(M, 2)
            print ('(',y+1, ',>) M=', M)
            print ("~~~~~~~~~~~~~~~~~~~~")
            
        elif last_three_bits == '101' or last_three_bits == '110':
            M = binary_addition(M[:A_bits], neg_A_bin_extended, A_bits) + M[A_bits:]
            print ('(',y+1, ',+) M=', M)
            M = arithmetic_shift_right(M, 2)
            print ('(',y+1, ',>) M=', M)
            print ("~~~~~~~~~~~~~~~~~~~~")
            
    return M[1:-1]
###########################################################################################################################
import sys

class RedirectStdout:
    def __init__(self, new_stdout):
        self.new_stdout = new_stdout
        self.original_stdout = sys.stdout

    def __enter__(self):
        sys.stdout = self.new_stdout

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.original_stdout

with open('in.txt', 'r') as file:
    with open('output.txt', 'w') as f:
        with RedirectStdout(f):
            n = file.readline().strip()
            for i in range(int(n)):
                m = file.readline().strip()
                b = file.readline().strip()
                s = file.readline().strip()
                A = file.readline().strip()
                B = file.readline().strip()
                print("-------------------------------")
                print ("out-",i)
                if int(m) == 0:
                    result = add_shift(int(b),int(s),int(A),int(B))
                    print ("M in Binary", result)
                    print ("M=AxB=", int(result,2))
                elif int(m) == 1:
                    result = booth_algorithm(int(b),int(s),int(A),int(B))
                    print ("M in Binary", result)
                    print ("M=AxB=", int(result,2))
                else:
                    print("operation not valid")
            print("-------------------------------")
