from heapq import heappush, heappop

def solve(threadCount, tasks):
    pq=[]
    maxTime=0
    for i in range(threadCount):
        heappush(pq,0)
    for task in tasks:
        time=heappop(pq)
        heappush(pq, time+task)
        maxTime=max(maxTime, time+task)
    return maxTime

def main():
    threadCount=3
    taskCount=[2, 2, 3, 7, 1, 5]
    taskCount.sort()
    result=solve(threadCount, taskCount)
    print(result)

if __name__ == "__main__":
    main()
