def handle_emergency_scenario(car_signal, pedestrian_signal, pedestrian_nearby, car_speed):
    """
    돌발 상황을 처리하는 시나리오
    car_signal: 차량 신호 ("RED", "YELLOW", "GREEN")
    pedestrian_signal: 보행자 신호 ("RED", "GREEN")
    pedestrian_nearby: 보행자 감지 여부 (True, False)
    car_speed: 차량 속도 (km/h 단위)
    """
    
    # 돌발 상황 1: 우회전 중 보행자 감지
    if car_signal == "GREEN" and pedestrian_nearby and car_speed > 5:
        print("경고: 우회전 중 보행자 감지됨. 즉시 속도 감속 및 정지 필요!")
        print("경고음 발생: 우회전 금지! 차량을 멈추세요.")
    
    # 돌발 상황 2: 신호등 고장 상태
    elif car_signal == "OFF" and pedestrian_signal == "OFF":
        print("신호등 고장: 모든 차량과 보행자는 교차로 진입 전 멈춰서 상황을 확인하세요.")
    
    # 돌발 상황 3: 차량 신호 초록불, 보행자 돌발 진입
    elif car_signal == "GREEN" and not pedestrian_nearby and car_speed > 20:
        print("주의: 차량 신호 초록불이지만 보행자 돌발 진입 가능성 있음.")
        print("속도를 줄이고 주변 환경을 살피세요.")

    # 돌발 상황 4: 속도 위반 차량 (과속)
    elif car_speed > 80:
        print("경고: 과속 중입니다! 즉시 속도를 줄이세요. 사고 위험 증가.")
        print("긴급 경고: 차량을 제어하지 못할 위험이 있습니다. 감속하세요.")
    
    else:
        print("긴급 상황 없음: 모든 조건 정상 작동 중.")
