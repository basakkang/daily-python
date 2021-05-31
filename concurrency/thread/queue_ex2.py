from queue import Queue
from threading import Thread

my_queue = Queue()

def consumer():
    print('소비자 대기')
    my_queue.get()  # 다음에 보여줄 put()이 실행된 다음에 시행된다
    print('소비자 완료')

thread = Thread(target=consumer)
thread.start()

print('생산자 데이터 추가')
my_queue.put(object())     # 앞에서 본 get()이 실행되기 전에 실행된다.
print('생산자 완료')
thread.join()

print('--------------')

from queue import Queue
from threading import Thread
import time

my_queue = Queue(1)  # 버퍼 크기 1

def consumer():
    time.sleep(0.1)  # 대기
    my_queue.get()  # 두 번째로 실행됨
    print('소비자 1')
    my_queue.get()  # 네 번째로 실행됨
    print('소비자 2')
    print('소비자 완료')

thread = Thread(target=consumer)
thread.start()

my_queue.put(object()) # 첫 번째로 실행됨
print('생산자 1')
my_queue.put(object()) # 세 번째로 실행됨
print('생산자 2')
print('생산자 완료')
thread.join()

print('--------------')

from queue import Queue
from threading import Thread
import time

in_queue = Queue()

def consumer():
    print('소비자 대기')
    work = in_queue.get()  # 두 번째로 실행됨
    print('소비자 작업중')
    # Doing work
    print('소비자 완료')
    in_queue.task_done()  # 세 번째로 실행됨

thread = Thread(target=consumer)
thread.start()

print('생산자 데이터 추가')
in_queue.put(object())    # 첫 번째로 실행됨
print('생산자 대기')
in_queue.join()           # 네 번째로 실행됨
print('생산자 완료')
thread.join()

print('--------------')
