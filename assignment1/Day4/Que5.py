conversion=[
   lambda t:t*1000,
   lambda kg:kg*1000,
   lambda gm:gm*1000,
   lambda mg:mg*0.00000220462
]
tonns=float(input("enter weight in tonns:"))
kg = conversion[0](tonns)
gm = conversion[1](kg)
mg = conversion[2](gm)
lbs = conversion[3](mg)

print("kilogram:",kg)
print("gram:",gm)
print("miligram:",mg)
print("pounds:",lbs)