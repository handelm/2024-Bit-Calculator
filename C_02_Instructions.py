# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instuctions
def instructions():
    statement_generator("instructions," "-")


print('''
Instructions go here.
-instruction 1 
-instruction 2
-instruction 3 
-etc
''')
# Main routine goes here


want_instructions = input ("Press <enter> to read the instructions or any key to continue ")

if want_instructions =="":
    instructions()

print("program continues")









