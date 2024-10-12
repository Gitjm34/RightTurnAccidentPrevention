def handle_traffic_scenario(car_signal, pedestrian_signal, pedestrian_nearby, car_speed):
    """
    차량 신호, 보행자 신호, 보행자 감지 상태, 차량 속도를 바탕으로 다양한 상황에 맞는 경고 메시지 출력
    car_signal: 차량 신호 ("RED", "YELLOW", "GREEN")
    pedestrian_signal: 보행자 신호 ("RED", "GREEN")
    pedestrian_nearby: 보행자 감지 여부 (True, False)
    car_speed: 차량 속도 (km/h 단위)
    """
    
    # 상황 1: 차량 신호 RED, 보행자 신호 RED, 보행자 감지
    if car_signal == "RED" and pedestrian_signal == "RED" and pedestrian_nearby:
        print("차량 신호: 빨간불, 보행자 신호: 빨간불 - 보행자 감지됨")
        print("경고: 차량 정지 상태 유지, 보행자 이동 경로 확인 필요.")
    
    # 상황 2: 차량 신호 RED, 보행자 신호 GREEN, 보행자 감지
    elif car_signal == "RED" and pedestrian_signal == "GREEN" and pedestrian_nearby:
        print("차량 신호: 빨간불, 보행자 신호: 초록불 - 보행자 감지됨")
        print("경고: 보행자 우선. 차량은 계속 정지. 주변을 주의 깊게 살피세요.")

    # 상황 3: 차량 신호 YELLOW, 보행자 신호 RED
    elif car_signal == "YELLOW" and pedestrian_signal == "RED":
        print("차량 신호: 노란불, 보행자 신호: 빨간불 - 보행자 없음")
        if car_speed > 30:
            print("경고: 속도가 높음! 감속 후 정차 준비하세요.")
        else:
            print("안전: 천천히 정차 준비 중입니다.")

    # 상황 4: 차량 신호 GREEN, 보행자 신호 RED, 보행자 감지 없음
    elif car_signal == "GREEN" and pedestrian_signal == "RED" and not pedestrian_nearby:
        print("차량 신호: 초록불, 보행자 신호: 빨간불 - 보행자 감지 안 됨")
        print("안전: 차량은 교차로를 서행하며 통과 중입니다.")

    # 상황 5: 차량 신호 GREEN, 보행자 신호 GREEN, 보행자 감지됨
    elif car_signal == "GREEN" and pedestrian_signal == "GREEN" and pedestrian_nearby:
        print("차량 신호: 초록불, 보행자 신호: 초록불 - 보행자 감지됨")
        if car_speed > 10:
            print("경고: 서행하거나 일시정지 후 보행자 확인 필요.")
        else:
            print("주의: 교차로 통과 시 주의 요망. 보행자와의 충돌 방지.")

    # 상황 6: 차량 신호 YELLOW, 보행자 신호 GREEN
    elif car_signal == "YELLOW" and pedestrian_signal == "GREEN":
        print("차량 신호: 노란불, 보행자 신호: 초록불 - 보행자 감지됨")
        print("경고: 차량은 정차 준비, 보행자는 빠르게 횡단하세요.")

    # 추가 시나리오: 보행자 감지가 되지 않더라도 차량 신호에 따라 적절한 조치 필요
    else:
        print("잘못된 상태: 차량과 보행자 신호 확인 필요.")
