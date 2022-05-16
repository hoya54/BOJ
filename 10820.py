

while True :
    try :
        st = list(input())

        lower, upper, num, blank = 0, 0, 0, 0

        for i in range(len(st)) :
            if st[i]  == " " :
                blank += 1
            elif 65 <= ord(st[i]) <= 90:
                upper += 1
            elif 97 <= ord(st[i]) <= 122:
                lower += 1
            else :
                num += 1
            
        print(lower,upper,num,blank)
    except EOFError :
        break