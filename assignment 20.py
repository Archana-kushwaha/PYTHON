def checkIsAP(series, n):
    if n == 1:
        return True

    series.sort()

    difference = series[1] - series[0]
    for i in range(2, n):
        if series[i] - series[i - 1] != difference:
            return False

    return True


series = [5, 7, 9, 11]
n = len(series)
print("True") if (checkIsAP(series, n)) else print("False")
