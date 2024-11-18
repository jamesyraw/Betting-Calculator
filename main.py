
# Online Python - IDE, Editor, Compiler, Interpreter

def sum(a, b):
    return (a * 2 ** b)

a = int(input('Enter initial bet: '))
b = int(input('Enter number of weeks: '))

print(f'If you bet ${a} for {b} weeks, you could win {sum(a, b)}')
