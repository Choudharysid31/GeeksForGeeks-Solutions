'''Given an array arr. Assume ‘0’ as the invalid number and all others as a valid number. Write a program that returns an array which is a modified version of the given array. 
The modification is done in such a way that if the current and next number are a valid number and are equal, double the current number value and replace the next number with 0.
After the modification, rearrange the array such that all 0's are shifted to the end and the sequence of the valid numbers is present in the same order.

Example:

Input: arr[ ] = [2, 2, 0, 4, 0, 8] 
Output : [4, 4, 8, 0, 0, 0] 
Explanation: At index 0 and 1 both the elements are the same. So, we will change the element at index 0 to 4 and the element at index 1 is 0 then we will shift all the zeros
to the end of the array. So, the array will become [4, 4, 8, 0, 0, 0].'''

    def modifyAndRearrangeArr (self, arr) :
        for i in range (len(arr)-1):
            if arr[i]==arr[i+1]:
                arr[i]=2*arr[i]
                arr[i+1]=0
        i=0
        for j in arr:
            if j!=0:
                arr[i]=j
                i+=1
        for k in range(i,len(arr)):
            arr[k]=0
        return arr
