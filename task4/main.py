import sys

file_1 = sys.argv[1]
nums = []

with open(file_1, 'r') as log:
  log_file = log.readlines()
  for line in log_file:
    nums.append(int(line.split('\n')[0]))

m = sorted(nums)[len(nums) // 2]
print(sum(abs(v - m) for v in nums))