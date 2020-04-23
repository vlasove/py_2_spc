from collections import Counter

c1 = Counter(a=2, b=3)
d1 = Counter(a=5, b=10)

print("Sum:",c1 + d1)
print("Sub:", d1 - c1)
print("Intersection:", c1 & d1)
print("Union:", c1 | d1)