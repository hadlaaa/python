d = {3:'C', 1:'A', 2:'B', 4:'D'}

desc = dict(sorted(d.items(), reverse=True))
print("Descending order:", desc)

d = {3:'C', 1:'A', 2:'B', 4:'D'}

asc = dict(sorted(d.items()))
print("Ascending order:", asc)
