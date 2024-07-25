'''Given an array arr consisting of only prime numbers, remove all duplicate numbers from it. 
Example:
Input: arr[] = [2, 2, 3, 3, 7, 5] 
Output: [2, 3, 7, 5]
Explanation: After removing the duplicates 2 and 3 we get 2 3 7 5.'''

def removeDuplicates(self, arr):
        uniq=[]
        for i in arr:
            if i not in uniq:
                uniq.append(i)
        return uniq
