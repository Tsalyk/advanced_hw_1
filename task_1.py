def equation(a1, a2, b1, b2, c1, c2):
    solutions_lst = []

    for i in range(a1, a2+1):
        for j in range(b1, b2+1):
            for k in range(c1, c2+1):
                if i != 0 or j != 0:
                    d = j**2 - (4 * i * k)

                    if d >= 0:

                        if i != 0:
                            x1 = (-j + (d ** (1/2))) / (2 * i)
                            x2 = (-j - (d ** (1/2))) / (2 * i)
                        else:
                            if j != 0:
                                x1 = x2 = -k / j

                        if int(x1) == 0:
                            x1 = 0
                        if int(x2) == 0:
                            x2 = 0

                        if x1 != x2:
                            solutions_lst.append([str(i), str(j), str(k),
                                                "Yes", str(round(x1, 2)),
                                                str(round(x2, 2))])
                        else:
                            solutions_lst.append([str(i), str(j), str(k),
                                                "Yes", str(round(x1, 2))])

    solutions_lst = list(map(lambda lst: " ".join(lst), solutions_lst))
    solutions = ""
    
    for element in solutions_lst:
        solutions += element + "\n"
    return solutions