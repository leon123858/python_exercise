from my_package.math.operation import square
from my_package.math.constant import PI

if __name__ == '__main__':
    print("i am main program")

radius = 5
area = square(radius)*PI
print(area)