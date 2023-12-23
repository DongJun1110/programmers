def solution(food):

  other = []
  answer = ''

  for i in range(len(food)):

      if i == 0: continue

      if food[i] == 1: continue
      else: 
          for j in range(food[i]//2):
              answer.append(food[i])
              other.append(food[i])

  other.reverse()

  for i in other:
    answer.append(i)

  return answer


  