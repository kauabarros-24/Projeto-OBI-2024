from queue import SimpleQueue
repeticoes = int(input())
q = SimpleQueue()
for i in range(repeticoes):
    expression = input()
    c = 0
    while c < len(expression) - 1:
        py = len(expression) - 1
        if expression[c] == "(" and expression[py] == ")" or expression[c] == "{" and expression[py] == "}" or expression[c] == "[" and expression[py] == "]":
            q.put("S")

        else:
            q.put("N")
        c+=1
        py-=1


while q.qsize() > 0:
    print(q.get())



    

    

    
