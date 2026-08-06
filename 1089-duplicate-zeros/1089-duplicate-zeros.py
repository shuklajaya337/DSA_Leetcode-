class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)

        l = len(arr) - 1
        r = len(arr) + zeros - 1

        while l < r:

            if r < len(arr):
                arr[r] = arr[l]

            if arr[l] == 0:
                r -= 1
                if r < len(arr):
                    arr[r] = 0

            l -= 1
            r -= 1