d = {'kritika': 10, 'harshita': 15, 'khushi': 20, 'ayushi':25}
sd = {}
myKeys = list(d.keys())
myKeys.sort()
for i in myKeys:
    sd[i] = d[i]
print(sd)
