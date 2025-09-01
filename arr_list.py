# 리스트를 위한 데이터
# 리스트의 데이터: 전역 변수
capacity = 100 # 리스트 용량: 예) 용량을 100으로 지정
array = [None] * capacity # 요소 배열: [None, .., None] (길이가 capacity)
size = 0

# 공백 상태 검사 isEmpty()
def isEmpty():
    if size == 0:
        return True # 공백이면 True 반환
    else:
        return False # 아니면 False 반환
    