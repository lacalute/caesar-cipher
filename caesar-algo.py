import string
import random

# the standart "classic" alphabet 
standart_alpha = list(string.ascii_lowercase)
# the alphabet, which will be changing for encoding process
encoding_alpha = list(string.ascii_lowercase)
# the alphabet, which will be changing for decoding process
decoding_alpha = list(string.ascii_lowercase)
# the lenght of decoding alphabet
poss = len(decoding_alpha)
# the coefficient K for encoding text (random)
k = random.randint(1, 25)

# the main class, which contains two methods: 
# 1. Encoding 
# - phrase (phrase, which you wanna encode)
# - key (the neccessary param for right encode process, any number from 0 to 25)
# method will return the encoded phrase
# 2. Decoding
# - phrase (phrase, which you wanna decode)
# method will return list of possible phrases, which you can find right phrase from
class Caesar:
  def encoding(self, phrase: str, key: int):
    # the list, which will contains encoded phrase
    result = []
    # first loop, 
    for o in range(0, key):
      ind = 0
      encoding_alpha.append(encoding_alpha[ind])
      encoding_alpha.remove(encoding_alpha[ind])

    for i in phrase.lower():
      if i != " ":
        result.append(encoding_alpha[decoding_alpha.index(i)])
      else:
        result.append(i)
    print("".join(result))

  def decoding(self, phrase: str):
    for n in range(1, poss):
      decoding_alpha = list(string.ascii_lowercase)
      result = []
      for n2 in range(0, n):
        ind = 0
        decoding_alpha.append(decoding_alpha[ind])
        decoding_alpha.pop(ind)  
      for i in phrase.lower():
        if i != " ":
          result.append(standart_alpha[decoding_alpha.index(i)])
        else:
          result.append(i)
      print(f"Iteration: {n}", "RESULT:", "".join(result))
# the obj
caesar = Caesar()





