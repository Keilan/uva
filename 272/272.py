import sys

#Track whether we are opening or closing
opening = True
for line in sys.stdin:
    out = ''
    for c in line:
        if c == '"':
            if opening:
                out += "``"
            else:
                out += "''"
            opening = not opening
        else:
            out += c
    sys.stdout.write(out)
