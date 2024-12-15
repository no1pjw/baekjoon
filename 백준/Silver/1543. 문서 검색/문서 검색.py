total_word = input()
total_word_len = len(total_word)
num = 0
find_word = input()
find_word_len = len(find_word)
find_count = 0
while num < total_word_len:
  temp_num = total_word.find(find_word, num)
  num = temp_num
  if temp_num == -1:
    break
  num += find_word_len
  find_count += 1
print(find_count)