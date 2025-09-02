class ArrayList: # 클래스 선언
    # 리스트의 데이터: 생성자에서 정의 및 초기화
    # __init__()에서 멤버 변수로 선언
    def __init__(self, capacity = 100): # 멤버 함수임을 나타내기 위해 첫번째 매개변수로 self 추가
    # 클래스의 멤버 함수에서 객체 자신의 데이터를 사용하거나 멤버 함수를 호출하기 위해 .self 추가
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    # 공백 상태 검사 isEmpty()
    def isEmpty(self):
        return self.size == 0

    # 포화 상태 검사 isFull()
    def isFull(self):
        return self.size == self.capacity

    # 삽입 연산 insert(pos, e)
    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else: pass

    # 삭제 연산 delete(pos)
    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size-1):
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else: pass

    # pos 위치의 항목을 참조 getEntry(pos)
    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else: return None

    # 문자열 변환 연산자 중복 함수 __str__()
    def __str__(self):
        return str(self.array[0:self.size])

# 테스트
if __name__ == "__main__":
    L = ArrayList(50) # 용량이 50인 리스트 객체를 만듦

    print("최초   ", L)
    L.insert(0, 10)
    L.insert(0, 20)
    L.insert(1, 30)
    L.insert(L.size, 40)
    L.insert(2, 50)
    print("삽입x5 ", L)
    L.delete(2)
    print("삭제(2)", L)
    L.delete(L.size-1)
    print("삭제(E)", L)
    L.delete(0)
    print("삭제(0)", L)