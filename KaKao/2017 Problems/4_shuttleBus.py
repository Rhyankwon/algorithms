class Solution:
    def shuttleBus(self, n, t, m, timetable):
        times = []
        for i in timetable:
            times.append(int(i[:2])*60 + int(i[3:]))
        times.sort()
        time = 540 + t * (n-1)
        candidate = 0
        for i in range(n):
            for j in range(m):
                if times and times[0] <= 540 + t * i:
                    candidate = times.pop(0)
                    candidate -= 1
                else :
                    candidate = 540 + t * i
        
        return str(candidate//60).zfill(2) + ':' + str(candidate%60).zfill(2)



timetable1 = ["08:00", "08:01", "08:02", "08:03"]
timetable2 = ["09:10", "09:09", "08:00"]
timetable3 = ["09:00", "09:00", "09:00", "09:00"]
timetable4 = ["00:01", "00:01", "00:01", "00:01", "00:01"]
timetable5 = ['23:59']
timetable6 = ["23:59", "23:59","23:59","23:59","23:59","23:59","23:59","23:59","23:59"]

solution = Solution()
print(solution.shuttleBus(1, 1, 5, timetable1))
print(solution.shuttleBus(2, 10, 2, timetable2))
print(solution.shuttleBus(2, 1, 2, timetable3))
print(solution.shuttleBus(1, 1, 5, timetable4))
print(solution.shuttleBus(1, 1, 1, timetable5))
print(solution.shuttleBus(10, 60, 45, timetable6))
