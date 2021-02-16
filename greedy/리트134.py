class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        fuel,start = 0,0
        
        for i in range(len(cost)):
            if fuel+gas[i]<cost[i]:
                start = i+1
                fuel = 0
            else:
                fuel += gas[i] -cost[i] #연료값 갱신
                
        return start
                
                
            
        