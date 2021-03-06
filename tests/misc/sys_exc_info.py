import sys
try:
    sys.exc_info
except:
    print("SKIP")
    sys.exit()

def f():
    print(sys.exc_info()[0:2])

try:
    1/0
except:
    print(sys.exc_info()[0:2])
    f()

# Outside except block, sys.exc_info() should be back to None's
f()

# Recursive except blocks are not handled - just don't
# use exc_info() at all, use explicit variables in "except".
