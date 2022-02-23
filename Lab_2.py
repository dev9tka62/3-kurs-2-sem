from time import time
from random import randint
from matplotlib import pyplot as plt

def genList(num, rand_range=1000):
  return [randint(0, rand_range) for i in range(0, num)]

def listStringization(some_list):
  out_string = ''
  for value in some_list:
    out_string += '  {:>10}'.format(value)
  return out_string

def bubble_sort(nums):  
  swapped = True
  while swapped:
    swapped = False
    for i in range(len(nums) - 1):
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
        swapped = True

def selection_sort(nums):  
  for i in range(len(nums)):
    lowest_value_index = i
    for j in range(i + 1, len(nums)):
      if nums[j] < nums[lowest_value_index]:
        lowest_value_index = j
    nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

def insertion_sort(nums):  
  for i in range(1, len(nums)):
    item_to_insert = nums[i]
    j = i - 1
    while j >= 0 and nums[j] > item_to_insert:
      nums[j + 1] = nums[j]
      j -= 1
    nums[j + 1] = item_to_insert

def heapify(nums, heap_size, root_index):  
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)
def heap_sort(nums):  
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

def merge(left_list, right_list):  
  sorted_list = []
  left_list_index = right_list_index = 0
  left_list_length, right_list_length = len(left_list), len(right_list)
  for _ in range(left_list_length + right_list_length):
    if left_list_index < left_list_length and right_list_index < right_list_length:
      if left_list[left_list_index] <= right_list[right_list_index]:
        sorted_list.append(left_list[left_list_index])
        left_list_index += 1
      else:
        sorted_list.append(right_list[right_list_index])
        right_list_index += 1
    elif left_list_index == left_list_length:
      sorted_list.append(right_list[right_list_index])
      right_list_index += 1
    elif right_list_index == right_list_length:
      sorted_list.append(left_list[left_list_index])
      left_list_index += 1
  return sorted_list
def merge_sort(nums):  
  if len(nums) <= 1:
    return nums
  mid = len(nums) // 2
  left_list = merge_sort(nums[:mid])
  right_list = merge_sort(nums[mid:])
  return merge(left_list, right_list)

def partition(nums, low, high):  
  pivot = nums[(low + high) // 2]
  i = low - 1
  j = high + 1
  while True:
    i += 1
    while nums[i] < pivot:
      i += 1
    j -= 1
    while nums[j] > pivot:
      j -= 1
    if i >= j:
      return j
    nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):  
  def _quick_sort(items, low, high):
    if low < high:
      split_index = partition(items, low, high)
      _quick_sort(items, low, split_index)
      _quick_sort(items, split_index + 1, high)
  _quick_sort(nums, 0, len(nums) - 1)

#----------------------------------------------------------------

lists_sizes = [100, 1000, 3000, 5000, 7000, 10000, 20000]
nums_lists = [genList(x) for x in lists_sizes]

sort_times = {
              'bubble sort': [],
              'selection sort': [],
              'insertion sort': [],
              'heap sort': [],
              'merge sort': [],
              'quick sort': [],
              'python sort': []
}

prog_start_time = time()

for key, value in sort_times.items():
  print('["{}" processing...]'.format(key.capitalize()))
  for l in range(0, len(nums_lists)):
    ten_times_time = 0
    for i in range(0, 10):
      if key == 'bubble sort':
        to_sort = nums_lists[l]
        s_time = time()
        bubble_sort(to_sort)
        e_time = time()
        f_time = e_time - s_time
        ten_times_time += f_time
      if key == 'selection sort':
        to_sort = nums_lists[l]
        s_time = time()
        selection_sort(to_sort)
        e_time = time()
        f_time = e_time - s_time
        ten_times_time += f_time
      if key == 'insertion sort':
        to_sort = nums_lists[l]
        s_time = time()
        insertion_sort(to_sort)
        e_time = time()
        f_time = e_time - s_time
        ten_times_time += f_time
      if key == 'heap sort':
        to_sort = nums_lists[l]
        s_time = time()
        heap_sort(to_sort)
        e_time = time()
        f_time = e_time - s_time
        ten_times_time += f_time
      if key == 'merge sort':
        to_sort = nums_lists[l]
        s_time = time()
        merge_sort(to_sort)
        e_time = time()
        f_time = e_time - s_time
        ten_times_time += f_time
      if key == 'quick sort':
        to_sort = nums_lists[l]
        s_time = time()
        quick_sort(to_sort)
        e_time = time()
        f_time = e_time - s_time
        ten_times_time += f_time
      if key == 'python sort':
        to_sort = nums_lists[l]
        s_time = time()
        sorted(to_sort)
        e_time = time()
        f_time = e_time - s_time
        ten_times_time += f_time
      nums_lists[l] = genList(len(nums_lists[l]))

    value.append(round(ten_times_time/10.0, 5))

fig, ax = plt.subplots()
ax.set_xlabel("Lists sizes")
ax.set_ylabel("Sorting time, s")

print('{:>30} {}'.format('Lists sizes:', listStringization(lists_sizes)))
for key, value in sort_times.items():
  print('{:>15} sorting times: {}'.format(key.capitalize(), listStringization(value)))
  ax.plot(lists_sizes, value, label=key)

prog_end_time = time()
total_time = round(prog_end_time - prog_start_time, 2)

minutes = int(total_time // 60)
secundes = round(total_time % 60, 1)
print("\n[ TOTAL TIME:   {} min {} sec ]".format(minutes, secundes))

plt.legend()
plt.show()