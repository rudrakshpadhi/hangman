#game of hangman

print('--------------------HANGMAN----------------------------')
word=input('User 1, enter the word\n').lower()
print('\n'*50)
word_list=[]
number_letters=len(word)
guess_list=[]
for n in word:
    word_list.append(n)
#print(word_list)



for i in word_list:
    if i==' ':
        guess_list.append(' ')
    else:
        guess_list.append('__')
wrong_guess=0
print(guess_list)

while wrong_guess in range(0,7):
    if '__' not in guess_list:
        quit()
    guess_letter=input('User 2,enter the guess letter\n')

    j=0
    while j<number_letters:
        if word_list[j]==guess_letter:
            guess_list[j]=guess_letter
        elif guess_letter not in word_list:
            wrong_guess=wrong_guess+1
            if wrong_guess==1:
                print('''
                            -----------------------------------------
                            |
                            |
                            |
                            O    ''')
                j=number_letters+1
            
            elif wrong_guess==2:
                print('''
                            -----------------------------------------
                            |
                            |
                            |
                            O
                            |
                                ''')
                j=number_letters+1
            elif wrong_guess==3:
                print('''
                            -----------------------------------------
                            |
                            |
                            |
                            O 
                         ---|   ''')
                j=number_letters+1
            elif wrong_guess==4:
                print('''
                            -----------------------------------------
                            |
                            |
                            |
                            O
                         ---|---   ''')
                j=number_letters+1
            elif wrong_guess==5:
                print('''
                            -----------------------------------------
                            |
                            |
                            |
                            O
                         ---|--- 
                           _|
                           |   ''')
                j=number_letters+1
            elif wrong_guess==6:
                print('''
                            -----------------------------------------
                            |
                            |
                            |
                            O
                         ---|--- 
                           _|_
                           |  |''')
                j=number_letters+1
                quit()
        j=j+1
    print(guess_list)
        



            
    

    






