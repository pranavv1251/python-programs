def generate(n):
    d = dict()
    for i in range(1, n+1):
        d[i] = i*i
    return d


def merge(d1, d2):
    d1.update(d2)
    print('The merged dict is: ', d1)
    return d1


# def sorting(d):
   # d.sort(key=lambda x: x.value())
  #  print(d)
  #  return d

def unique_val(di):
    print(set(di.values()))


def highest(d):
    print(sorted(d, reverse=True)[:3])


n = int(input('Enter the value of n: '))
di = generate(n)
print(di)
di = merge(di, {6: 25, 7: 49})
unique_val(di)
highest(di)
print(sorted(di.items))
