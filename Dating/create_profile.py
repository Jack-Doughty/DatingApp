import sys, os
def create_profile():
    impquestions = ['Name?','Gender?', 'Age?', 'Gender preference?']
    impanswers = []
    for i in impquestions:
        impanswers.append(input(i).lower())
    print('Answer in a scale of 0 to 9.')
    questions = ['How much do you like sports?', 'How much do you like gaming?', 'How much do you like animals?', 'How rich are you?', 'How close do you live to Burford? (London is a 6)']
    answers = []
    for y in questions:
        answers.append((input(y)).lower()) #scale of 0 to 9
    f = open((str(impanswers[0]) + '.txt'), "w")
    for j in range (len(impanswers)):
        f.write(str(impanswers[j]) + ' ')
    f.write('$ ')
    for x in range (len(answers)):
        f.write(str(answers[x]) + ' ')
    f.close()
