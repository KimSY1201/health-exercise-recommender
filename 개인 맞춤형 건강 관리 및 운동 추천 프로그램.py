## ---------------------------------------------------------
## 개인 맞춤형 건강 관리 및 운동 추천 프로그램
## ---------------------------------------------------------
## 개발범위 : 개인의 BMI계산 및 하루에 섭취해야 할  탄/단/지 양 계산(탄/단/지 양에 따른 음식 추천 )
##           그리고 개인의 목표와 운동 강도의 설정에 따른 운동 추천 
## UI 형식 : 명령어기반 CUI/TUI=> Terminal
## UI 메뉴 : 이름, 나이, 성별, 몸무게, 키, 관리 목표 
## 기능구현 : BMI계산 및 하루 권장 섭취 칼로리 계산 및 개인별 운동 추천
## --------------------------------------------------------- 
 
import datetime
import bmi_function

print('\n','\n',' '*5,'개인 맞춤형 건강 관리 및 운동 추천 프로그램',' '*5,'\n')
print(' '*30,'made 김수연','\n','\n')
print('< 개인정보 입력하기 >\n')

# 사용자 정보 입력 받기
name, age, gender, weight, height, goal = bmi_function.get_user_info()

# 올바른 데이터 입력인지 확인
# age변수

if len(name)>0:
     if len(age)>0 and age.isdecimal():
          age = int(age)
# gender변수     
          if len(gender)>0 and gender.isalpha():
# weight변수
               if len(weight)>0:
                    weight = int(weight)
# height변수
                    if len(height)>0:
                         height = int(height)
# goal변수
                         if len(goal)>0:
                              pass
else:
     print('데이터를 잘못입력하셨습니다.')

   
print(f'< {name}님 맞춤형 건강 관리 및 운동 추홍길천 프로그램 상세 설명 >','\n')



# BMI & 기초대사량 보여주기
print(f"\n\n1. 신체질량지수(BMI)와 기초대사량",'\n')


# BMI 계산   
BMI = weight/((height/100)**2)

# BMI 범위
if BMI >=30:
     level = '고도비만'
elif BMI >=25:
     level = '비만'
elif BMI >= 23:
     level = '과체중'
elif BMI >=18.5:
     level = '정상'
else:
     level = '저체중'

# 기초대사량 계산
if gender == '남자':
     bmr_cal = 66.47+(13.75*weight)+(5*height)-(6.76*age)
elif gender == '여자':
     bmr_cal = 665.1+(9.56*weight)+(1.85*height)-(4.68*age)

print(f'{name}님의 신체질량지수(BMI)는 {round(BMI,2)}로 {level}입니다.')
print(f'{name}님의 기초대사량은 {round(bmr_cal,2)}kcal입니다.','\n')

# 추천 하루 식단 가이드
print(f"2.{name}님께 추천하는 하루 식단 가이드",'\n','\n')


# 하루에 섭취해야하는 탄수화물, 단백질, 지방 섭취량 계산 
# 단백질
protein = (weight*1.8)
# 하루 권장 섭취 칼로리
if gender == '남자':
      allday_kcal = (10*weight)+(6.25*height)-(5*age)+5
elif gender == '여자':
     allday_kcal =(10*weight)+(6.25*height)-(5*age)-161
# 지방
fat = round((allday_kcal*0.2)/9,2)
# 탄수화물
carbohydrate = round((allday_kcal-protein-fat)/4,2)

# 하루 추천 섭취량 보여주기
print(f'-----하루 추천 섭취량-----\n- 탄수화물 :{carbohydrate}g 단백질 : {protein}g 지방 : {fat}g\n')
# 하루 추천 섭취량 보여주기(2끼 섭취시)
print(f'<하루 2끼 식사 시 : 일일 섭취 열량 {allday_kcal} = {round((allday_kcal/2),2)} X 2끼>')
print(f'- 탄수화물 :{round((carbohydrate/2),2)}g 단백질 : {round((protein/2),2)}g 지방 : {round((fat/2))}g','\n')
# 하루 추천 섭취량 보여주기(2끼 섭취시)
print(f'<하루 3끼 식사 시> : 일일 섭취 열량 {allday_kcal} = {round((allday_kcal/3),2)} X 3끼>')
print(f'- 탄수화물 :{round((carbohydrate/3),2)}g 단백질 : {round((protein/3),2)}g 지방 : {round((fat/3))}g','\n')
# 종류별 음식 추천(탄수화물)
print('* 탄수화물 섭취 추천 음식')
print('- 사과, 고구마, 감자, 바나나, 현미밥, 오트밀, 자몽, 통밀식빵\n')
# 종류별 음식 추천(단백질)
print('* 단백질 섭취 추천 음식')
print('- 두부, 낫또, 연어, 닭가슴살, 닭안심살, 돼지안심, 소우둔, 계란\n ')
# 종류별 음식 추천(지방)
print('* 지방 섭취 추천 음식')
print('- 치즈, 아보카도, 올리브유, 아몬드, 등푸른생선,\n ')

# 운동 추천
workouts = bmi_function.recommend_workout(age, goal)
print("\n- 추천 운동:")
for workout in workouts:
      print(f"{workout}")

# 건강 팁 제공
tips = bmi_function.health_tips(age,gender)
print("\n- 건강 팁:")
for tip in tips:
     print(f"{tip}")

current = datetime.datetime.now()
current_time = current.strftime('%Y-%m-%d %H:%M:%S')     
print(f'\n\n      {name}님의 맞춤형건강 관리 및 운동 추천 프로그램 ({current_time})     ')