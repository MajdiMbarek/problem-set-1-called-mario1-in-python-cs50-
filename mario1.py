
def main():
    height = get_height()
    for i in range(height):
        print((height - 1 - i )* " ", end="")
        print((i + 1 )* "#")


def get_height():
    while True:
        height = int(input("height: "))
        if height > 0 :
            break
    return height


main()

