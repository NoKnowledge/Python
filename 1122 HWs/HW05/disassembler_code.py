#Jimmy Lauchoy
#CS1122
#HW05

def disassemble(operation_code):
    string_code = str(operation_code)
    mnemonic = ""
    if string_code == "901":
        mnemonic = "INP"
        return mnemonic
    elif string_code == "902":
        mnemonic = "OUT"
        return mnemonic
    elif string_code == "000":
        mnemonic = "END"
        return mnemonic
    elif string_code[0] == "1":
        mnemonic = "ADD " + string_code[1] + string_code[2]
        return mnemonic
    elif string_code[0] == "2":
        mnemonic = "SUB " + string_code[1] + string_code[2]
        return mnemonic
    elif string_code[0] == "3":
        mnemonic = "STA " + string_code[1] + string_code[2]
        return mnemonic
    elif string_code[0] == "5":
        mnemonic = "LDA " + string_code[1] + string_code[2]
        return mnemonic
    elif string_code[0] == "6":
        mnemonic = "BRA " + string_code[1] + string_code[2]
        return mnemonic
    elif string_code[0] == "7":
        mnemonic = "BRZ " + string_code[1] + string_code[2]
        return mnemonic
    elif string_code[0] == "8":
        mnemonic = "BRP " + string_code[1] + string_code[2]
        return mnemonic
    else:
        error = str(operation_code) + " could not be found."
        return error

    # this function should take in an integer operation code
    # and convert it to a LMC mnemonic instruction and return
    # it as a string

def main():
    run = True
    list = []
    while run == True:
        code = input("Type your operation code: ")
        if code != 000:
            list.append(code)
        elif code == 000:
            for i in list:
                result = disassemble(i)
                print(result)
            exit_code = disassemble("000")
            print(exit_code)
            run = False

    # The main function should read all operation codes from the
    # user until the HLT instruction is read. Once it is read,
    # all operation codes should be disassembled using "disasassembled"
    # and then printed out to the user

main()
