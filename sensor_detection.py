import RPi.GPIO as GPIO
import time

# 초음파 센서 핀 설정
TRIG = 23  # 초음파 송신 핀
ECHO = 24  # 초음파 수신 핀
MAX_DISTANCE = 300  # 최대 측정 거리(cm)
SAFE_DISTANCE = 50  # 안전 거리 기준(cm)

# GPIO 핀 설정 및 초기화
GPIO.setmode(GPIO.BCM)  # GPIO 모드 설정 (BCM 핀 번호 사용)
GPIO.setup(TRIG, GPIO.OUT)  # TRIG 핀을 출력 모드로 설정
GPIO.setup(ECHO, GPIO.IN)   # ECHO 핀을 입력 모드로 설정

# 거리 측정 함수
def measure_distance():
    # 초음파 신호 전송
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # 10us 동안 신호 전송
    GPIO.output(TRIG, False)

    # 신호 수신 시간 계산
    start_time = time.time()
    while GPIO.input(ECHO) == 0:
        start_time = time.time()
    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    # 초음파 왕복 시간을 기반으로 거리 계산
    time_elapsed = end_time - start_time
    distance = (time_elapsed * 34300) / 2  # 음속 34300cm/s로 거리 계산
    return distance

# 메인 실행 코드
try:
    while True:
        dist = measure_distance()
        print(f"Measured Distance: {dist:.1f} cm")

        # 거리에 따른 메시지 출력
        if dist < SAFE_DISTANCE:
            print("Warning: 보행자 감지 -> 차량 정지 필요")
        elif dist < MAX_DISTANCE:
            print("Caution: 주위 환경 확인 필요")
        else:
            print("All clear: 주변에 감지된 물체 없음")

        # 1초에 한 번씩 측정
        time.sleep(1)

except KeyboardInterrupt:
    print("측정 중단. GPIO 핀 초기화 중...")
    GPIO.cleanup()  # GPIO 핀 설정 초기화
    print("GPIO 핀 초기화 완료.")
