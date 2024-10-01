import pandas as pd

# CSV 파일 읽기
speed_data = pd.read_csv(r"C:/Users/SM-PC/Desktop/2024_2/MEIT/2020_평균속도_행정구역.csv")
congestion_cost_data = pd.read_csv(r"C:/Users/SM-PC/Desktop/2024_2/MEIT/2020년_교통혼잡비용_행정구역.csv")

# 데이터 병합
merged_data = pd.merge(speed_data, congestion_cost_data, on=['sido_code', 'sigungu_code', 'emd_code'])

# 필터링 기준
optimal_speed_threshold = 30  # km/h 이하의 속도
low_congestion_threshold = merged_data['ALL_cost_CG'].quantile(0.25)  # 상위 25%의 혼잡도가 낮은 값

# 속도가 적당하고 혼잡도가 낮은 데이터를 필터링
optimal_time_data = merged_data[(merged_data['velocity_AVRG'] <= optimal_speed_threshold) & 
                                (merged_data['ALL_cost_CG'] <= low_congestion_threshold)]

# 데이터를 CSV 파일로 저장
optimal_time_data.to_csv("C:/Users/SM-PC/Desktop/2024_2/MEIT/optimal_robot_driving_time.csv", index=False)

# 또는 데이터를 콘솔에 출력
print(optimal_time_data)
