import torch
import cv2
import time

# YOLOv5 모델 로드 (사전 학습된 모델 사용)
print("YOLOv5 모델을 로드 중입니다...")
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
print("모델 로드 완료!")

# 카메라 장치 열기
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: 카메라를 열 수 없습니다.")
    exit()

# 초당 프레임(fps) 측정을 위한 초기화
frame_count = 0
start_time = time.time()

# 객체 인식 루프 시작
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: 프레임을 읽어올 수 없습니다.")
        break
    
    # YOLOv5 모델을 통한 객체 감지 수행
    frame_count += 1
    results = model(frame)

    # 객체 감지 결과 렌더링
    results.render()

    # 초당 프레임(fps) 계산
    if frame_count >= 10:  # 10 프레임마다 fps를 계산
        elapsed_time = time.time() - start_time
        fps = frame_count / elapsed_time
        frame_count = 0
        start_time = time.time()

        # FPS를 프레임에 표시
        cv2.putText(results.imgs[0], f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # 인식 결과 화면에 출력
    cv2.imshow('YOLOv5 Object Detection', results.imgs[0])

    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) == ord('q'):
        break

# 카메라 장치 및 모든 윈도우 종료
cap.release()
cv2.destroyAllWindows()
