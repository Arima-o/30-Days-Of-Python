# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("---")
print(len(it_companies))
it_companies.update({'Twitter'})
print(it_companies)
it_companies.pop()
print(it_companies)
print("---")

# A.update(B)
# print(A)
print(A.issubset(B))
print(A.isdisjoint(B))
del A
del B
# print(A)
print("---")

ageset = set(age)
print(ageset)
print(len(ageset) == len(age))
if len(ageset) > len(age):
    print("Ageset is greater")
elif len(age) > len(ageset):
    print("Age is greater")