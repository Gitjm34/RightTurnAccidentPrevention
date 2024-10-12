def handle_weather_scenario(weather, time_of_day, road_condition, car_speed):
    """
    날씨, 시간대 및 도로 상태에 따른 차량 동작 처리
    weather: 날씨 상태 ("SUNNY", "RAINY", "SNOWY", "FOGGY")
    time_of_day: 시간대 ("DAY", "NIGHT")
    road_condition: 도로 상태 ("DRY", "WET", "ICY")
    car_speed: 차량 속도 (km/h 단위)
    """

    # 눈이 오거나 도로가 미끄러운 상태
    if weather == "SNOWY" or road_condition == "ICY":
        print("경고: 도로가 미끄럽습니다. 차량 속도를 즉시 줄이세요.")
        if car_speed > 30:
            print("경고: 속도가 너무 빠릅니다. 감속하세요.")
    
    # 안개가 끼어 가시거리가 짧은 경우
    elif weather == "FOGGY":
        print("주의: 가시거리가 짧습니다. 전방 주의 및 서행 필요.")
    
    # 비 오는 날, 도로가 젖어 있는 경우
    elif weather == "RAINY" and road_condition == "WET":
        print("주의: 도로가 젖어 있습니다. 브레이크 제어에 주의하세요.")
        if car_speed > 50:
            print("경고: 속도를 줄이세요. 미끄러질 위험이 있습니다.")

    # 야간 운전 시
    if time_of_day == "NIGHT":
        print("주의: 야간 운전 중입니다. 전방 주의 및 라이트 사용을 확인하세요.")
        if car_speed > 60:
            print("경고: 야간 속도 제한을 초과 중입니다. 즉시 감속하세요.")

    else:
        print("날씨 및 도로 상태 양호. 정상 운행 중입니다.")
