def complexFormat(comp):
    r, img = int(comp.real), int(comp.imag)
    return "%s %s %si" % (r, "-" if img < 0 else "+", abs(img))


for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    A, B = complex(a, b), complex(c, d)
    print(complexFormat((A+B)*A), complexFormat((A+B)*(A+B)), sep=", ")