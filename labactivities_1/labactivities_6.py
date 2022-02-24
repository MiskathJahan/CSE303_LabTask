#Define the function
def add_two(x):
    x += 2
    print(x)
add_two(5)

def f(*args, **kwargs):
    y = args[0]
    z = kwargs.get("y")
    print (f"y: {y}, z: {z}")
 f(5, y=2)