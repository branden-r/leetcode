class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        # i < j < k, so the sequence must go nums[i], nums[j], nums[k]
        # however, nums[i] < nums[k] < nums[j]
        nums_i: int = nums[0]  # first number has to be nums[i]
        nums_k: int  # last number we find will be nums[k], so use this to iterate
        stack: list[tuple[int, int]] = []  # use the stack to save potential values for (nums[i], nums[k])
        for nums_k in nums[1:]:  # skip the first element since we already stored it in nums[i]
            while stack and stack[-1][1] <= nums_k:  # delete any tuples where nums[j] is too low
                del stack[-1]
            if stack and stack[-1][0] < nums_k:  # if the stack is not empty, we have a good value for nums[j]
                return True  # if we have a good value for nums[i] as well, we are done
            # we didn't find a solution
            stack.append((nums_i, nums_k))  # store nums[i] and nums[j] on the stack to try them later
            nums_i = min(nums_i, nums_k)  # we want nums[i] as low as possible, so update that too
        return False
