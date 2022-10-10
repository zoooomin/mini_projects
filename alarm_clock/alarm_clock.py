##설치할 라이브러리
'''
pip3 install playsound
pip3 install pyobjc
'''
##오디오 파일
###원하는 오디오 파일을 프로젝트와 같은 폴더에 넣어 사용해줘야함
from datetime import datetime
from playsound import playsound
alarm_time = input('enter the time of alarm to be set:HH:MM:SS\n')
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
print('setting complete')
while True:
    now = datetime.now()
    current_hour = now.strftime('%H')
    current_minute = now.strftime('%M')
    current_seconds = now.strftime('%S')
    if (alarm_hour == current_hour):
        if (alarm_minute == current_minute):
            if (alarm_seconds == current_seconds):
                print('it\'s time to dance!')
                playsound('audio.mp3')
                break
