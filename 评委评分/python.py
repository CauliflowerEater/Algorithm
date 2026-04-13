"""
题目拆解：
1.  输入处理，将输入的评分矩阵存为每个选手的分数数组；
    每个选手对象存id，总分，以及倒序排列的分数集;
2.  排序器，按总分排序，总分相同按分数集排序;

仅仅这样是不够的，因为我写出了排序器，但是仅通过了50%的测试用例；
还需要进行排序优化;
"""
from heapq import heappush, heappop

class Player:
    def __init__(self, id):
        self.id=id
        self.totalScore=0
        self.scores=[]

def createPlayerSet(scores):
    m=len(scores)
    n=len(scores[0])

    playerSet={}

    for i in range(m):
        for j in range(n):
            if j+1 not in playerSet:
                playerSet[j+1]=Player(j+1)
            heappush(playerSet[j+1].scores, -scores[i][j])
            playerSet[j+1].totalScore+=scores[i][j]
    return playerSet

def sortPlayerSet(playerSet):
    #对s.scores*(-1)是因为，此前利用取相反数来实现heapq的大根堆排序；此处需要将score恢复为原值;
    #sorted() API默认是升序排序，reverse=True表示降序排序，而list则是按照字典序来降序排序;
    return sorted(playerSet.values(), key=lambda x: (x.totalScore, x.scores*(-1)), reverse=True)

def main():
    scores=[[10, 9, 8, 7], [0, 1, 2, 3], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    playerSet=createPlayerSet(scores)
    sortedPlayerSet=sortPlayerSet(playerSet)
    for i in range(3):
        print(sortedPlayerSet[i].id, end=" ")

if __name__ == "__main__":
    main()

"""
大根堆的实现方式:
1. 在入堆时，将元素取负值入堆，出堆时，将元素取负值出堆；利用小跟堆来伪造大根堆；
2. 存tuple，存第一个值为优先级，第二个值为实际值；只需将第一个值取为实际值的相反数即可；
3. 自实现排序类；
最干净的方法是第一个，但是第二个的逻辑最清晰，看情况；

排序器的语法是这题的第二个实现关键点;
不仅仅是python的，java的也需要看看;
sorted(arr,key=lambda x: (x.totalScore, -x.scores),reverse=True)
其中lambda规定的排序规则;
默认是升序排序的，通过取相反数来实现降序；

"""