import sys

#Find the perfect squares with a given number of digits
def getQuirksomeSquares():
    #Start by getting the perfect squares
    squares = {2:[], 4:[], 6:[], 8:[]}
    num = 0;
    square = num*num
    while square < 1e8:
        squares[8].append(square)
        if square < 1e6:
            squares[6].append(square)
        if square < 1e4:
            squares[4].append(square)
        if square < 1e2:
            squares[2].append(square)

        num += 1
        square = num*num

    #Filter to only include quirksome squares - note that format(x, '08') pads up to 8 zeros
    def isQuirksome(n, digits):
        string_n = format(n, '0' + str(digits))
        return (int(string_n[:(digits//2)]) + int(string_n[-(digits//2):])) ** 2 == n

    for digits, square_nums in squares.items():
        temp = filter(lambda x:isQuirksome(x, digits), square_nums)
        squares[digits] = list(map(lambda x:format(x, '0' + str(digits)), temp))

    return squares


def main():
    squares = getQuirksomeSquares()
    for line in sys.stdin:
        n = int(line)
        for s in squares[n]:
            print(s)

if __name__ == '__main__':
    main()
