'''Given an array of strictly positive integers, 
    check if we can split it into two subsets that have an equal sum
'''
import heapq
from common import time_execution
from collections import deque


@time_execution()
def partition_dp(nums):
    # If we can't split the sum in 2 equal integer parts then we can't have 2 partitions with same sum
    half_sum, remainder = divmod(sum(nums), 2)
    if remainder:
        return False

    dp = [False] * (half_sum + 1)
    # We can always sum up to 0 by not taking anything
    dp[0] = True

    for num in nums:
        # By going in reverse, we make sure we didn't use current number twice
        for current_sum in range(half_sum, num - 1, -1):
            if dp[current_sum - num]:  # If we can reach current_sum-num, we can also reach current_sum
                dp[current_sum] = True
                if current_sum == half_sum:  # Early return if we reached half of the sum
                    return True

    return False


@time_execution()
def partition_rec(nums: list[int]) -> bool:
    def helper(sum1: int, sum2: int, idx: int) -> bool:
        if idx == len(nums):
            return sum1 == sum2

        return helper(sum1+nums[idx], sum2, idx+1) or helper(sum1, sum2+nums[idx], idx+1)

    return helper(0, 0, 0)


@time_execution()
def partition_rec_v2(nums: list[int]) -> bool:
    def helper(sum_so_far: int, idx: int) -> bool:
        if idx == len(nums):
            return False
        if sum_so_far == half_sum:
            return True

        return helper(sum_so_far+nums[idx], idx+1) or helper(sum_so_far, idx+1)

    half_sum, remainder = divmod(sum(nums), 2)
    if remainder:
        return False
    return helper(0, 0)


@time_execution()
def partition_memo(nums: list[int]) -> bool:
    memo = {}
    memo_count = 0

    def helper(sum_so_far: int, idx: int) -> bool:
        nonlocal memo_count
        if idx == len(nums):
            return False
        if sum_so_far == half_sum:
            return True

        key = (sum_so_far, idx)
        if key in memo:
            memo_count += 1
            return memo[key]

        memo[key] = helper(sum_so_far+nums[idx], idx +
                           1) or helper(sum_so_far, idx+1)
        return memo[key]

    half_sum, remainder = divmod(sum(nums), 2)
    if remainder:
        return False
    return f"{helper(0, 0)}, memo_count: {memo_count}"


@time_execution()
def partition_memo_v2(nums: list[int]) -> bool:
    memo = {0: True}
    memo_count = 0

    def helper(remainder: int) -> bool:
        nonlocal memo_count
        if remainder in memo:
            memo_count += 1
            return memo[remainder]

        for num in nums:
            if (rem := remainder-num) >= 0:
                if helper(rem):
                    return True

        memo[remainder] = False
        return False

    # If we can't split the sum in 2 equal integer parts then we can't have 2 partitions with same sum
    half_sum, remainder = divmod(sum(nums), 2)
    if remainder:
        return False

    return f"{helper(half_sum)}, memo_count: {memo_count}"


@time_execution()
def partition_bfs(nums: list[int]) -> bool:
    # If we can't split the sum in 2 equal integer parts then we can't have 2 partitions with same sum
    half_sum, remainder = divmod(sum(nums), 2)
    if remainder:
        return False

    queue = deque([(0, 0)])
    while queue:
        sum_so_far, idx = queue.popleft()

        for i in range(idx, len(nums)):
            new_sum = sum_so_far+nums[i]
            if new_sum == half_sum:
                return True
            if new_sum < half_sum:
                queue.append((new_sum, i+1))

    return False


@time_execution()
def partition_dijkstra(nums: list[int]) -> bool:
    # If we can't split the sum in 2 equal integer parts then we can't have 2 partitions with same sum
    half_sum, remainder = divmod(sum(nums), 2)
    if remainder:
        return False

    pq = []
    heapq.heappush(pq, (0, 0))
    while pq:
        sum_so_far, idx = heapq.heappop(pq)
        for i in range(idx, len(nums)):
            new_sum = sum_so_far-nums[i]
            if new_sum == -half_sum:
                return True
            if new_sum > -half_sum:
                heapq.heappush(pq, (new_sum, i+1))

    return False


nums = [5, 7, 9, 1, 4, 5, 6, 7]
print(partition_dp(nums))
print(partition_rec(nums))
print(partition_rec_v2(nums))
print(partition_memo(nums))
print(partition_memo_v2(nums))
print(partition_bfs(nums))
print(partition_dijkstra(nums))
