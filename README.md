Group Members Details:-

Nutan Kumari- 2022341
Pandillapelly - 2022345
Nikhil Rathore - 2022321
Priyanshu Yadav - 2022383

This is the repository for our group project for computer organization course .
We have added all the three folders which were given to us. And it contains the main script "Assembler.py" inside the Simple-Assembler folder , the run file inside it also contains the mentioned commands to run . But by chance , if anything fails then we have added the main script "Assembler.py" as alone to the repository . Although everthing is working fine from our end .

// 7th june 2023 //

new functions we created:

clear register (clr) -> opcode (11001) <5 bits opcode> <11 unused bits>

add imm to reg (adi reg1 $imm) -> opcode (11110) <5 bits opcode> <1 unused bit> <3 bit reg> <7 bit imm >

exponential ( pow reg1 reg2 reg3 ) -> opcode (10011) <5 bits opcode> <2 unused bit> <3 bit reg> <3 bit reg> <3 bit reg>

increment ( inc reg ) -> opcode (10100) <5 bits opcode> <8 unused bit> <3 bit reg>

decrement ( dec reg ) -> opcode (10101) <5 bits opcode> <8 unused bit> <3 bit reg>
