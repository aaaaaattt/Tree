#힙은 배열구조로, 0번째 인덱스는 비어두기 root가 인덱스 1임
heap=[0,4,3,2,1]
print(len(heap))

#최대 힙의 삽입 연산
def heappush(heap, n) :
    heap.append(n)  #n을 리스트 heap의 맨 뒤에 삽입
    i = len(heap)-1 #i는 n이 삽입된 위치, 0번째 index는 무시하므로 -1
    while i != 1:   #루트까지 올라가지 않았으면 up-heap 과정 진행
        pi = i//2   #부모 노드의 위치
        if n <= heap[pi]:   #부모보다 작으면 올라가기 종료
            break
        heap[i] = heap[pi]  #부모를 자식 위치로 내려버림
        i = pi              #i가 부모인덱스로 바뀜
    heap[i] = n             #마지막 위치에 n삽입