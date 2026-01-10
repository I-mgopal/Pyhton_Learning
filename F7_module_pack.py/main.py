from f1_import_module import get_X
cal = 2* get_X()
print(cal)
# import f2_operation
# print(f2_operation.addition(12,13))
# print(f2_operation.multiplication(12,13))
from f2_operation import addition,multiplication
print(addition(12,13))


#Packages
# from modules1 import increasing_op,decreasing_op
# print(increasing_op.square1(12))
# print(decreasing_op.sqrt1(144))

# from modules1.model import hello
# hello.hello()


#if use __init__.py then
from modules1 import square1, sqrt1, hello

print(square1(12))
print(sqrt1(144))
hello()
