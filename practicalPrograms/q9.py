a=10

def local():
    global a
    b=100
    c = a+b
    print(f"global veriable {a} + Local veriable { b} : addition {c}")

local()