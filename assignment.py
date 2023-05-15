registers={"FLAGS":"111","R6":"110","R5":"101","R4":"100","R3":"011","R2":"010","R1":"001","R0":"000"}
opcodes={"hlt":"11010","je":"11111","jgt":"11101","jlt":"11100","jmp":"01111","cmp":"01110","not":"01101","and":"01100","or":"01011",
        "xor":"01010", "ls":"01001","rs":"01000","div":"00111","mul":"00110","st":"00101","ld":"00100","movC":"00011","movB":"00010","sub":"00001","add":"00000"}
file = open("co.txt", 'r')
def remove_empty(l):
    c = l.count('\n')
    for i in range(c):
        l.remove('\n')
    return l
instruction =remove_empty(file.readlines())
file.close()
error=''
memory_dict={}
var_dict={}

def countoccurrences(str, word):
    a = str.split()
    count = 0
    for i in range(0, len(a)):
        if (word == a[i]):
           count = count + 1
            
    return count 

