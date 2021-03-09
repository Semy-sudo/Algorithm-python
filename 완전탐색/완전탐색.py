def solution(answers):
  answer = []
  answer_1 = [1,2,3,4,5]
  answer_2 = [2,1,2,3,2,4,2,5]
  answer_3 = [3,3,1,1,2,2,4,4,5,5]

  scores = [0,0,0]

  for i in range(len(answers)):
    if answer_1[i%5] == answers[i]:
      scores[0]+=1
    if answer_2[i%8] == answers[i]:
      scores[1]+=1
    if answer_3[i%10] == answers[i]:
      scores[2]+=1

  for person,score in enumerate(scores):
    if score == max(scores):
      answer.append(person+1)

  return answer






answers = [1,2,3,4,5]
print(solution(answers))