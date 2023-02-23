class Solution:
    def twoSum(self, numbers, target: int):
        leftPtr, rightPtr = 0, len(numbers) - 1

        while leftPtr < rightPtr:
            if numbers[leftPtr] + numbers[rightPtr] == target:
                return [leftPtr + 1, rightPtr+1]
            elif numbers[leftPtr] + numbers[rightPtr] > target:
                rightPtr -= 1
            elif numbers[leftPtr] + numbers[rightPtr] < target:
                leftPtr += 1