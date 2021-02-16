#heapq.heappush(heap,값) #최소힙
#result.insert(인덱스,[값])
import heapq
import List

def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
  heap = []
  #people 최소힙으로 정렬
  for person in people:
    heapq.heappush(heap,(-person[0],person[1])) #최대힙 만들기 위해

    # [-7,0],[-7,1],[...]

  result = []
  while heap:
    person = heapq.heappop(heap)
    result.insert(person[1],[-person[0],person[1]])

  return result

