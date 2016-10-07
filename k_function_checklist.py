import random
import chalk

YES = ['y', 'Y', 'yes', 'Yes', 'yy']
NO = ['n', 'N', 'no', 'No', 'nn']


class Question(object):
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        self.checked = False

    def __repr__(self):
        if self.checked == False:
            message = "Unanswered Question"
        else:
            message = "Checked Question"
        return message

    def check(self):
        self.checked = True
        return self

    def ask(self):
        response = input(self.prompt)
        if response in self.answer:
            self.check()
        elif response in NO:
            pass # something ....
        else:
            print("what..?")

        return self


def main(shuffle=False):
    '''
    Creates many question objects and asks the user to answer them until all questions are successfully answered.
    '''
    a = Question("Did you start your function definition with def?", YES)
    b = Question("Does your function name have only characters and _ (underscore) characters?", YES)
    c = Question("Did you put an open parenthesis ( right after the function name?", YES)
    d = Question("Did you put your arguments after the parenthesis ( separated by commas?", YES)
    e = Question("Did you make each argument unique (meaning no duplicated names)?", YES)
    f = Question("Did you put a close parenthesis and a colon ): after the arguments?", YES)
    g = Question("Did you indent all lines of code you want in the function four spaces? No more, no less.", YES)
    h = Question("Did you 'end' your function by going back to writing with no indent (dedenting we call it)?", YES)
    i = Question("Did you call/use/run this function by typing its name?", YES)
    j = Question("Did you put the ( character after the name to run it?", YES)
    k = Question("Did you put the values you want into the parenthesis separated by commas?", YES)
    l = Question("Did you end the function call with a ) character?", YES)

    checklist = [a, b, c, d, e, f, g, h, i, j, k, l]
    counter = 0
    while len(checklist) > 0:
        for question in checklist:
            question.ask()
            if question.checked is True:
                checklist.remove(question)
            counter += 1

        if len(checklist) > 0:
            chalk.warning('Keep Going...')

    chalk.yellow("Hooray! Your function checklist is complete. You answered {tries} questions.".format(tries=counter))
    return True


def intro():
    '''
    Runs the main menu...
    '''
    chalk.yellow("Let's go through the steps of creating a function.\nAnswer YES for yes or 'N' for no")
    chalk.red("Defining your function: ")
    main()
    return True

intro()
