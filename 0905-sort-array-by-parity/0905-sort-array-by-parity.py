class Solution:
    def sortArrayByParity(self, arr: List[int]) -> List[int]:
        n=len(arr)
        i=0
        mid=0
        j=n-1

        while mid<=j:
            if arr[mid]%2!=0:
                arr[mid],arr[j]=arr[j],arr[mid]
                j-=1
            else:
                arr[mid],arr[i]= arr[i], arr[mid]
                mid+=1
                i+=1

        return arr

        