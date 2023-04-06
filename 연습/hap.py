def calc(v1, v2, op) :
    match (op) :
        case ("+") :
            return v1 + v2
        case ("-") :
            return v1 - v2
        case ("*") :
            return v1 * v2
        case ("/") :
            return v1 / v2
        case (_) :
            return "ERROR"

l = [int(input("1st : ")), str(input("op : ")), int(input("2nd : "))]

print(calc(l[0], l[2], l[1]))