import pandas as pd

# 엑셀 파일 읽기
file_path = r"C:\Python\Pet_Culture_Data20221130.xlsx"
data=pd.read_excel(file_path)

#데이터 확인
#print(data.head())

#'시군구 명칭'에서 '강남구'에 해당하는 행 필터링
filtered_data = data[(data['시군구 명칭'] == '강남구') & ((data['카테고리2'] == '반려동물식당카페') | (data['카테고리2'] == '반려동반여행'))]
print(filtered_data[['시설명', '카테고리3', '도로명주소', '전화번호']])
