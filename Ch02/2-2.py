"""
    날짜 : 2020/06/22
    이름 : 박수령
    내용 : 문자열 자료형 실습하기  p44
"""
# 문자열 더하기
str1 = 'Hello '
str2 = 'Python!'
str3 = str1 + str2
print('str3 : ', str3)

# 문자열 곱하기
str = 'python!'
print('str * 5 : ', str * 5)

# 문자열 길이
hello = 'Hello World'
print('hello 길이 : ', len(hello))

# 문자열 인덱스
print('hello[0] : ', hello[0])
print('hello[6] : ', hello[6])

# 문자열 슬라이스
print('hello[0:7] : ', hello[0:7])
print('hello[1:7] : ', hello[1:7])
print('hello[:7] : ', hello[:7])
print('hello[7:] : ', hello[7:])
print('hello[-1] : ', hello[-1])
print('hello[-2] : ', hello[-2])

# 문자열 분리
animal = '사자,호랑이,코끼리,기린'
a1, a2, a3, a4 = animal.split(',')

print('a1 :', a1)
print('a2 :', a2)
print('a3 :', a3)
print('a4 :', a4)

# 문자열 포맷
fm1 = '오늘은 %d월 입니다.'
fm2 = '오늘은 %d월 %d일 입니다.'
fm3 = '오늘은 %s월 입니다.'
fm4 = '오늘은 %s년 %d월 %d일 %s요일 입니다.'

print(fm1 % 6)
print(fm2 % (6, 22))
print(fm3 % '06')
print(fm4 % ('2020', 6, 22, '월'))

# 문자열 관련 함수 p67 ~ p71
# 문자 개수 세기(count)
a = "hobby"
a.count('b')
print('a: ', a.count('b')) # 문자열에서 b의 갯수 >>2

# 위치 알려주기 1(find)
a = "Python is the best choice"
a.find('b')
print('a: ', a.find('b')) # 문자열에서 b가 처음 나온 위치 >>14

a.find('k')
print('a: ', a.find('k')) # 찾는 문자나 문자열이 존재하지 않는다면 -1을 반환한다. >> -1

# 위치 알려주기 2(index)
a = "Life is too short"
a.index('t')
print('a: ', a.index('t')) # 찾는 문자나 문자열의 위치를 알려준다.>>8

# a.index('k')
# print('a: ', a.index('k')) # 찾는 문자 'k'가 없기 때문에 오류 발생..

# 문자열 삽입(join)

# 소문자를 대문자로 바꾸기(upper)
a = "hi"
a.upper()
print('a: ', a.upper())

# 대문자를 소문자로 바꾸기(lower)
a = "Hi"
a.lower()
print('a: ', a.lower())

# 왼쪽 공백 지우기(lstrip)
a = " hi "
a.lstrip()
print('a: ', a.lstrip())
