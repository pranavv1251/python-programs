def countstr(s):
    l = s.split()
    for i in l:
        print(f'{i} occurence: {l.count(i)}')


countstr('hello i am hello')
