class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            j = i + 1
            while j < len(numbers) and numbers[j] < (target - numbers[i]):
                j += 1
            
            if j < len(numbers) and numbers[j] == target - numbers[i]:
                return [i + 1, j + 1]
