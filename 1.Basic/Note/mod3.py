PI = 3.141592

class Math:
    def solve(self,r):   #class에 함수를 정의 할때는 무조건 self가 들어가야한다. 값을 불러올때는 필요없음
        return PI * (r**2)  #원의 면적구하기
    def sum(self, a, b):
        return a + b
# // reference

if __name__ == "__main__": # main
    print(PI)
    a = Math()
    print(a.solve(2))
    print(a.sum(PI, 4.4))
# // 실행, 우클릭 run python terminal 실행