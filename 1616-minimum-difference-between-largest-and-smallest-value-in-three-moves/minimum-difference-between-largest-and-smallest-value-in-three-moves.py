def minDifference(nums):
    n = len(nums)
    if n <= 4:
        return 0
    nums.sort()
    mi, ma = nums[0], nums[-1]
    a = ma - nums[3]
    b = nums[n - 4] - mi
    c = nums[n - 3] - nums[1]
    d = nums[n - 2] - nums[2]
    return min(a, b, c, d)

f = open('user.out','w')
for i in map(loads,stdin):
    f.write(f'{minDifference(i)}\n') 
f.flush()
exit(0)