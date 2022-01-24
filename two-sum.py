class Solution:

    #brute force method. O(n^2) runtime.
    def bruteSolver(nums, target) -> int[2]:
        for x in range(0, len(nums)):
            for y in range(1, len(nums)):
                if (nums[x] + nums[y] == target):
                    return [x,y]

    #hashtable lookup method. O(n) runtime.
    def solver(nums, target) -> int[2]:
        dict = {target - nums[0]: 0}

        for i in range(1, len(nums)):
            if (nums[i] in dict and dict[nums[i]] != i):
                return [dict[nums[i]], i]
            else:
                dict[target - nums[i]] = i


nums = [2,7,11,15]
target = 26

print(Solution.bruteSolver(nums, target))
print(Solution.solver(nums, target))