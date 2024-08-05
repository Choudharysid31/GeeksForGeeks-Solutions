'''Given an unsorted array arr of size n of positive integers. One number 'A' from set {1, 2,....,N} is missing and one number 'B' occurs twice in array. 
Find these two numbers.
Your task is to complete the function findTwoElement() which takes the array of integers arr and n as parameters and returns an array of integers of size 2 denoting the answer
(The first index contains B and second index contains A)

Examples
Input: n = 2 arr[] = {2, 2}
Output: 2 1
Explanation: Repeating number is 2 and smallest positive missing number is 1.
Input: n = 3 arr[] = {1, 3, 3} 
Output: 3 2
Explanation: Repeating number is 3 and smallest positive missing number is 2.'''

    def findTwoElement( self,arr, n): 
        brr=sum(set(arr))
        sume=len(arr)*(len(arr)+1)//2
        miss=sume-brr
        repeat=(sum(arr)+miss)-sume
        return (repeat,miss)
