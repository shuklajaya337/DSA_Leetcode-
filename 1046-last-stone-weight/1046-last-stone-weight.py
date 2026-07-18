class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones.sort()

            larger = stones[-1]
            second_larger = stones[-2]

            stones.remove(larger)
            stones.remove(second_larger)

            if larger != second_larger:
                stones.append(larger - second_larger)

        if len(stones) == 0:
            return 0

        return stones[0]
        