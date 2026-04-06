#难点在于对输入的处理，输入的时间格式是202411231010，即YYYYMMDDHHMM格式的时间，不能直接作为数值来对待；
#本题考察的是对时间字符串的处理，可以用SimpleDateFormat("yyyyMMddHHmm")来处理;
#题干说明了，查询区间内存在未覆盖的时间点；
#这题是”给出若干区间“，”查询某一区间“，并且查询区间未必完全覆盖，未知点位跳过；
#思路：
#求遍历报告区间，逐一与查询区间求交集，按交集逐一时间点添加KPI值到结果集；
#报告区间不必有序，只要保证结果集有序即可；
#问题拆解成：
#1. 将输入的报告区间转化为日期的格式；
#2. 求交集的方法；
#3. 按步长遍历区间并添加到结果集;
#4. 结果集排序；
#5. 将结果转化回YYYYMMDDHHMM格式的时间字符串进行输出;

from datetime import datetime, timedelta
import heapq


def toDate(timeStr):
    return datetime.strptime(timeStr, "%Y%m%d%H%M")

def toTimeStr(date):
    return datetime.strftime(date, "%Y%m%d%H%M")

def getIntersection(reportInterval, queryInterval):
    return max(reportInterval[0], queryInterval[0]), min(reportInterval[1], queryInterval[1])
#日期是可以比较大小的，因此对两个日期区间求交集，就是求起始日期的较大值，和终止日期的较小值；

def getResult(reportIntervals, queryInterval):
    result = []
    for reportInterval in reportIntervals:
        intersection = getIntersection(reportInterval, queryInterval)
        if intersection[0] <= intersection[1]:#如果intersection[0] > intersection[1],则代表，其中一个区间的起始值大于另一区间的终止值，交集不存在；
            addToResultSet(result, intersection, reportInterval[2])
    return result

def addToResultSet(resultSet, intersection, kpiValue, step_minutes=1):
    #range()仅能遍历整数，因此需要通过timedelta定义step来实现按步长遍历;
    start, end = intersection[0], intersection[1]
    step = timedelta(minutes=step_minutes)
    t = start
    while t <= end:
        heapq.heappush(resultSet, (t, kpiValue))
        t += step

def main():
    queryInterval=[toDate("202411231010"), toDate("202411231013")]
    reportIntervals=[
        [toDate("202411231000"), toDate("202411231010"), 11],
        [toDate("202411231011"), toDate("202411231012"), 10],
        [toDate("202411231013"), toDate("202411231020"), 16],
        [toDate("202411231021"), toDate("202411231028"), 17],
    ]
    result = getResult(reportIntervals, queryInterval)
    while result:
        time, kpiValue = heapq.heappop(result)
        print(toTimeStr(time), kpiValue)

if __name__ == "__main__":
    main()


f"""
在优化方案中，
用result={}
将结果集存储为字典，key为时间，value为KPI值；
然后对result按key排序，将结果按格式输出；
对map进行排序，这是py区别于java的特性；
"""