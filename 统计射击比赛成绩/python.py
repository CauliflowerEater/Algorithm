"""
题目拆分:
1. 处理输入，输入两个list，一个代表id，一个代表分数，按照位置一一对应，将输入存为player对象;
2. 求得每个选手的前三位总分之和;
3. 对所有选手按照总分进行降序排序，分数相等按照ID进行降序排序;

"""

class Player:
    def __init__(self, id, scores):
        self.id=id
        self.scores=scores
        self.top3Sum=0

def createPlayerSet(ids, scores):
    playerSet={}
    for i in range(len(ids)):
        if ids[i] not in playerSet:
            playerSet[ids[i]]=Player(ids[i], [])
        playerSet[ids[i]].scores.append(scores[i])
    return calculateTop3Sum(playerSet)

def calculateTop3Sum(playerSet):
    to_remove = [pid for pid, p in playerSet.items() if len(p.scores) < 3]
    for pid in to_remove:
        playerSet.pop(pid)
    for player in playerSet.values():
        player.top3Sum=sum(sorted(player.scores, reverse=True)[:3])
    return playerSet

def sortPlayerSet(playerSet):
    return sorted(playerSet.values(), key=lambda x: (x.top3Sum, x.id), reverse=True)

def main():
    ids=[1,2,1,2,1,2]
    scores=[10, 20, 30, 40, 50, 60]
    playerSet=createPlayerSet(ids, scores)
    sortedPlayerSet=sortPlayerSet(playerSet)
    for player in sortedPlayerSet:
        print(player.id, end=" ")
    print()

if __name__ == "__main__":
    main()

"""
对scores<3的player的删除操作，注意不能在遍历的过程中动态删除;
player.top3Sum=sum(sorted(player.scores, reverse=True)[:3])
注意这个写法；
"""