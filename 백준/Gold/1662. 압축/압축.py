word = input()
global word_len, bracket_count, multiple_list, number_list
word_len = len(word)
bracket_count = 0
multiple_list = [0] * 50
number_list = [0] * 50
def _word(word, present_index):
  global word_len, bracket_count, multiple_list, number_list
  if present_index == word_len:
    pass
  else:
    if word[present_index] == "(":
      bracket_count += 1
      multiple_list[bracket_count] = int(word[present_index - 1])
      number_list[bracket_count - 1] -= 1
    elif word[present_index] == ")":
      bracket_count -= 1
      number_list[bracket_count] += multiple_list[bracket_count + 1] * number_list[bracket_count + 1]
      multiple_list[bracket_count + 1] = 0
      number_list[bracket_count + 1] = 0
    else:
      number_list[bracket_count] += 1
    _word(word, present_index + 1)
_word(word, 0)
print(number_list[0])
