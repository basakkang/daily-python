def iam_generator():
    print('참을성 있게')
    yield '기다리자'


obj = iam_generator()
print(1)

output = next(obj)
print(2)

print(output)
print(3)