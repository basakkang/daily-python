import subprocess

result = subprocess.run(['echo', '자식 프로세스에 노내는 인사!'],
    capture_output=True,
    encoding='utf-8'
)

result.check_returncode()
print(result.stdout)

proc = subprocess.Popen(['sleep', '1'])
while proc.poll() is None:
    print('작업 중..')

print('종료 상태', proc.poll())
