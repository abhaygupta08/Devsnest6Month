from questions import QUESTIONS
import os
import random



def removekey(d, key):
    r = dict(d)
    del r[key]
    return r


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    if question['answer']==answer:
        return True
    else:
        return False
    # return True if answer == 2 else False      #remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    ss = ques
    answ = "option"+str(ss['answer'])
    toMayRem = ["option1","option2","option3","option4"]
    toMayRem.remove(answ)
    # ss = removekey(ss,answ)
    for i in range(2):
        rem = random.choice(toMayRem)
        ss = removekey(ss,rem)
        toMayRem.remove(rem)
    return ss


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    won = 0
    lifeLineLeft = 1
    os.system('cls')
    print('\n\n\t\t\t ULTIMATE KBC GAME\n\n\t\t\t Lacks only Amit ji\n\n')
        
    for i in range(15):
        curr = str(i+1)
        print('\tQuestion '+curr+': '+QUESTIONS[i]["name"] )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = ""
        while ans=="":
            print('Your choice ( 1-4 )',end="")
            if lifeLineLeft:
                print(' [0 for LifeLine 50:50 ] : ',end="")
            else:
                print(' : ',end="")
            ans = input()

        if ans=="0" and lifeLineLeft:
            lifeLineLeft -= 1
            newQ = lifeLine(QUESTIONS[i])
            print('\tQuestion '+curr+': '+newQ["name"] )
            print(f'\t\tOptions:')
            for k,v in newQ.items():
                if k.startswith('option'):
                    print('\t\t\tOption',k[-1],':',v)
            ans = ""
            while ans=="" or ans=="0":
                ans = input('Your choice ( 1-4 ): ')
        if ans=="0" and lifeLineLeft==0:
            print("NO LIFE-LINE LEFT")
            while int(ans) not in range(1,5):
                ans = input('Your choice ( 1-4 ) : ')
        
        # check for the input validations
        if isAnswerCorrect(QUESTIONS[i], int(ans) ):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            won += int(QUESTIONS[i]["money"])
            print('\nCorrect !','WON :',won)

        else:
            # end the game now.
            # also print the correct answer
            print('\nIncorrect !')
            print("CORRECT answer was :",QUESTIONS[i]["option"+str(QUESTIONS[i]["answer"])])
            break
        # os.system('cls')

    
    print('\nCongratulation you Won :',str(won),'(in total)')


kbc()

