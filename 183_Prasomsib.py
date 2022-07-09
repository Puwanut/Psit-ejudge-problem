"""PrasomSib"""
def method_sum10(nums):
    """find amount of method can make 10 in num"""
    count = 0
    for i in range(len(nums)):
        total = 0
        for num in nums[i:]:
            total += int(num)
            if total == 10:
                count += 1
            elif total > 10:
                break
    print(count)
method_sum10(input())
