''' You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i and end[i] is the finish time of meeting i. 
Return the maximum number of meetings that can be accommodated in a single meeting room, when only one meeting can be held in the meeting room at a particular time. 

Note: The start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

Examples :

Input: n = 6, start[] = [1, 3, 0, 5, 8, 5], end[] =  [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2), (3, 4), (5,7) and (8,9)
Input: n = 3, start[] = [10, 12, 20], end[] = [20, 25, 30]
Output: 1
Explanation: Only one meetings can be held with given start and end timings.
Expected Time Complexity: O(n*logn)
Expected Auxilliary Space: O(n)'''

    def maximumMeetings(self,n,start,end):
        meeting=[]
        count=0
        for i in range(n):
            meeting.append([end[i],start[i]])
        meeting.sort()
        endtime=meeting[0][0]
        count=1
        for i in range(n):
            if meeting[i][1]>endtime:
                count+=1
                endtime=meeting[i][0]
        return count
