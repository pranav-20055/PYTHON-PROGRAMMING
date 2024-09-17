def solve(nums):
    count=0
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] == nums[j]:
                count+=1
    return count
k = 2
nums =[7,1,5,3,6,4]
print(solve(nums))
