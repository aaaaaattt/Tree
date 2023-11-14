#힙은 배열구조로, 0번째 인덱스는 비어두기 root가 인덱스 1임


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



heap=[0,4,3,2,1]

def heappop(heap) :
    size = len(heap) -1
    if size == 0:
        return None
    
    pi = 1                  #부모 노드의 인덱스
    i = 2                   #왼쪽 자식 인덳
    root = heap[1]          #삭제할 루트 노드(사장)
    last = heap[size]       #마지막 노드(말단사원)

    while i<= size:         #더 내려갈 자식이 있을 때까지 down-heap 진행
        if i<size and heap[i] < heap[i+1]:  #오른쪽 놈이 더 크면
            i += 1                          #down-heap은 오른쪽 자식에 대해 처리
        if last >= heap[i]:                 #자식이 더 작으면 종료
            break
        heap[pi] = heap[i]                  #더 큰 자식을 부모위치로 끌어올림
        pi = i                              #부모 위치가 자식 위치 i로 내려감
        i *= 2                              #자식은 일단 부모의 왼쪽 자식

    heap[pi] = last                         #맨 마지막 노드를 parent 위치에 복사
    heap.pop()                              #맨 마지막 노드 삭제
    return root                             #저장해 두었던 루트를 반환


#허프만 코딩 트리 만들기
def make_tree(freq):
    heap = [0]
    for n in freq :
        heappush(heap,n)

    for i in range(1, len(freq)) :
        e1 = heappop(heap)
        e2 = heappop(heap)
        heappush(heap, e1 + e2)
        print("(%d+%d)" %(e1,e2))

label = ['E', 'T', 'N', 'I', 'S']
freq = [15, 12, 8, 6, 4] #정렬된 배열임
make_tree(freq)
