"""
题目拆分:
1. 设计外循环代表比赛的轮次;
2. 设计内循环代表轮内的比赛场次;
3. 设计内外循环的桥梁;
4. 处理轮空队伍的边界情况;
5. 定位季军的方式;

这题的难点在于定位季军;

思路整理：
冠军是最后一轮比较中胜出的队伍；
亚军是在决赛中失败的队伍；
季军是在与冠军的半决赛中失败的队伍；
相对于性能优化和代码的间接，这题中写出逻辑清晰的代码才是最重要的；
季军的产生依赖于冠军所处的子树，可以通过冠军的对决历史来决定季军；
取季军需要一个额外的数据结构；

可以优化为，仅依赖History来取亚军和季军，而最小化对战过程；

"""
class Team:
    def __init__(self, id, score):
        self.id = id
        self.score = score
        self.history = []

def fight(teams):
    size=len(teams)
    winners=[]
    for i in range(0, size, 2):
        #处理补偿为2的遍历中可能存在的末尾奇数edgecase;
        # 只要i==size-1，就可以捕捉到末尾奇数进行处理;
        if i==size-1:
            winners.append(teams[i])
            continue

        team1=teams[i]
        team2=teams[i+1]
        if team2.score>team1.score:
            winners.append(team2)
            team2.history.append(team1.id)
        else:
            winners.append(team1)
            team1.history.append(team2.id)
    return winners

def main():
    input=[99, 98, 92, 97, 96, 96, 95]
    teams=[Team(i, input[i]) for i in range(len(input))]
    while len(teams)>1:
        teams=fight(teams)
    winner=teams[0]
    second=winner.history.pop()
    third=winner.history.pop()
    print(winner.id, second, third)

if __name__ == "__main__":
    main()

"""
核心trick:
1. 发现亚军和季军的共同特点是存在于冠军的对决历史中；因此可以用history来定位亚军和季军；

memo:
1. 原位操作是优化而不是必须； 相对于性能优化，代码的易读性和逻辑的连贯性更重要；
2. 类和成员变量相对于二维数组可以更直观的表达逻辑，也更具拓展性；
"""