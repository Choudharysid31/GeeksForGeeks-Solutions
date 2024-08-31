'''Given two sorted arrays arr1 and arr2 and an element k. The task is to find the element that would be at the kth position of the combined sorted array.

Input: k = 5, arr1[] = [2, 3, 6, 7, 9], arr2[] = [1, 4, 8, 10]
Output: 6
Explanation: The final combined sorted array would be - 1, 2, 3, 4, 6, 7, 8, 9, 10. The 5th element of this array is 6.

Input: k = 7, arr1[] = [100, 112, 256, 349, 770], arr2[] = [72, 86, 113, 119, 265, 445, 892]
Output: 256
Explanation: Combined sorted array is - 72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892. 7th element of this array is 256.

Expected Time Complexity: O(log(n) + log(m))
Expected Auxiliary Space: O(log (n))'''

class Solution:
    def kthElement(self, k, arr1, arr2):
        i=0
        j=0
        arr=[]
        n=len(arr1)
        m=len(arr2)
        while i<n and j<m:
            if len(arr)==k:
                return(arr[k-1])
            if arr1[i]<arr2[j]:
                arr.append(arr1[i])
                i+=1
            elif arr2[j]<arr1[i]:
                arr.append(arr2[j])
                j+=1
            else:
                arr.append(arr1[i])
                arr.append(arr2[j])
                i+=1
                j+=1
        while i<n:
            arr.append(arr1[i])
            i+=1
        while j<m:
            arr.append(arr2[j])
            j+=1
        return arr[k-1]
