
nums = [1,2,3,4]

out = []
p = 1
# 왼쪽 곱셈
for i in range(0, len(nums)):
    out.append(p)
    p = p * nums[i]

p = 1
# 오른쪽 곱셈
for i in range(len(nums)-1, -1, -1):
    out[i] *= p
    p *= nums[i]
print(out)