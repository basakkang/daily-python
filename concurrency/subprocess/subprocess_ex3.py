import subprocess
import os

# 시스템에 openssl을 설치하지 않은 경우에는 작동하지 않을 수 있다.
def run_encrypt(data):
    env = os.environ.copy()
    env['password'] = 'zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE, # 파이프를 통해서 입력받을 것
        stdout=subprocess.PIPE)
    proc.stdin.write(data) # 파이프를 통해서 입력 받는 부분
    proc.stdin.flush() # 자식이 입력을 받도록 보장한다
    return proc

procs = []
for _ in range(3):
    data = os.urandom(10) # size 10 random bytes
    proc = run_encrypt(data)
    procs.append(proc)

for proc in procs:
    out, _ = proc.communicate() # stdout과 stderr에서 데이터를 읽는 부분.
    print(out[-10:])