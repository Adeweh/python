def twoSum(nums: list, value: int) -> list:
    """ A method that adds two int together and returns a list  """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == value:
                return [i, j]


def two_sum(nums: list, value: int) -> list:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            res = nums[i] + nums[j]
            if value == res:
                return [i, j]


def two_s(nums: list, value: int) -> list:
    map_ = {}
    for i in range(len(nums)):
        complement = value - nums[i]

        if complement in map_:
            return [map_[complement], i]
        else:
            map_[nums[i]] = 1
    return []


lst = [3, 1, 5, -8]
value = 6

print(twoSum(lst, value))
print(two_sum(lst, value))
print(two_s(lst, value))
help(twoSum)
