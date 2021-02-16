#리트코드122
import List

def maxProfit(self, prices: List[int])-> int:
  #어차피 0보다 크면 매번 더하기
  return sum(max(prices[i+1]-prices[i],0) for i in range(len(prices)-1))