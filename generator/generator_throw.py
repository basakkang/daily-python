class MyError(Exception):
    pass

def my_generator():
    yield 1
    yield 2
    yield 3

it = my_generator()
print(next(it))  # 1을 내놓음
print(next(it))  # 2를 내놓음
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
print(it.throw(MyError('test error')))
