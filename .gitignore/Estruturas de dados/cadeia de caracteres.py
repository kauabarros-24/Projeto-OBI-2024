
repet = int(input())

for _ in range(repet):
    palavra = input()
    str = []
    ok = "S"
    for c in palavra:
        if c in "([{":
            str.append(c)
        else:
            if len(str) > 0 and str[-1] == "(" and c == ")":
                str.pop()
            elif len(str) > 0 and str[-1] == "[" and c == "]":
                str.pop()
            elif len(str) > 0 and str[-1] == "{" and c == "}":
                str.pop()
            else:
                ok = "N"
                break
    if len(str) > 0:
        ok = "N"
    print(ok)

