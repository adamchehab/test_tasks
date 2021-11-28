import sys

file_1 = sys.argv[1]
file_2 = sys.argv[2]

# read from file1 (circle)
with open(file_1, 'r') as log:
  log_file = log.readlines()
  O_x = float(log_file[0].split(' ')[0])
  O_y = float(log_file[0].split(' ')[1])
  O_r = float(log_file[1].split(' ')[0])

r_should = O_r**2
answer_list = []

# read from file2
with open(file_2, 'r') as log:
  log_file = log.readlines()
  for line in log_file:
    a = float(line.split(' ')[0])
    b = float(line.split(' ')[1])
    r = (O_x - a)**2 + (O_y - b)**2

    # write answers to answers list
    if r == r_should:
      answer = 0
    elif r < r_should:
      answer = 1
    elif r > r_should:
      answer = 2
    answer_list.append(answer)


# print answers list
print(answer_list)