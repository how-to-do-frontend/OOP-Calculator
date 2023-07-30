from Add import Add
from Subtract import Subtract
from Multiply import Multiply
from Divide import Divide

operations = [Add, Subtract, Multiply, Divide]

op = int(input('[1] Add [2] Subtract [3] Multiply [4] Divide: '))

op1 = int(input('Number 1: '))
op2 = int(input('Number 2: '))

op = operations[op-1](op1, op2)
print(op.execute())