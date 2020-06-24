"""
    날짜 : 2020/06/24
    이름 : 박수령
    내용 : 모듈 p207
"""
import  Ch05.sub1.Calc as calc

# 파이썬 프로그램 시작
if __name__=="__main__":

    # 모듈(파이썬 패키지에 있는 소스파일) 함수 호출
    rs1 = Calc.plus(1, 2)
    rs2 = Calc.minus(1, 2)
    rs3 = Calc.multi(2, 3)
    rs4 = Calc.minus(4, 2)

    print('rs1 :', rs1)
    print('rs2 :', rs2)
    print('rs3 :', rs3)
    print('rs4 :', rs4)