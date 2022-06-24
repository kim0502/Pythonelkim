def sum(a, b):
    if type(a) != type(b):
        print("더하기를 할 수 없습니다.")
    else:
        return a + b

if __name__ == "__main__":  # 메인모듈
    print(sum(10,20)) 