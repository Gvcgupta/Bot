from hangman import Hangman

hang=Hangman()



while hang.wrongs>=0:

    hang.ask(hang.sol,hang.word)
    hang.display(hang.sol)
    if hang.check==False:
        hang.wrongs=-1
    if hang.wrongs<0:
        print("chances are over")
        print("right answer is",end=" ")
        hang.rightAnswer(hang.word)
