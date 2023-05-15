          if (i[0]=='mov'):
            if(i[2][0]=='R' or i[2]=='FLAGS'):
                i[0]='movC'
            else:
                i[0]='movB'
        text+=opcodes[i[0]]
        if i[0]=='add' or i[0]=='mul' or i[0]=='sub' or i[0]=='xor' or i[0]=='or' or i[0]=='and':
            if len(i)!=4:
                general_syntax_error(inputline)
            text=typeA(i, text, inputline)
            binarygeneratedcode.append(text)

        elif ((i[0]=='movB' and i[2][0]=='$') or i[0]=='rs' or i[0]=='ls'):
            if len(i)!=3:
                general_syntax_error(inputline)
            text = typeB(i, text, inputline)
            binarygeneratedcode.append(text)
        elif (i[0]=='movC') or i[0]=='div' or i[0]=='cmp' or i[0]=='not':
            if len(i)!=3:
                general_syntax_error(inputline)
            text=typeC(i, text, inputline)
            binarygeneratedcode.append(text)
        elif (i[0]=='ld') or i[0]=='st':
            if len(i)!=3:
                general_syntax_error(inputline)
            text = typeD(i, text, inputline)
            binarygeneratedcode.append(text)
        elif i[0]=='jmp' or i[0]=='jlt' or i[0]=='jgt' or i[0]=='je':
            if len(i)!=2:
                general_syntax_error(inputline)
            text=typeE(i, text, inputline)
            binarygeneratedcode.append(text)
        elif i[0]=='hlt':
            if len(i)!=1:
                general_syntax_error(inputline)
            text=typeF(i, text, inputline)
        else:
            typing_error_instruction(inputline)
    else:
        if inputline<=counter:
            pass
        else:
            # print(counter)
            # print(inputline)
            error="variables not declared at the beginning"
with open("machinecode.txt", 'a') as f:
    if (error==""):
        for k in binarygeneratedcode:
            f.write(f"{k}")
            f.write("\n")
    else:
        f.write(error)
    for i,y in var_dict.items():
        f.write(f"{i}:{y}")
        f.write("\n")
