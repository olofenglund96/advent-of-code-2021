with open("./input", "r") as file:
  lines = [int(line.strip()) for line in file.readlines()]

c = 0
prevsum = 10000000
for v1, v2, v3 in zip(lines[:-2], lines[1:-1], lines[2:]):
  csum = sum([v1, v2, v3])
  if prevsum < csum:
    c += 1

  prevsum = csum


print(c)
