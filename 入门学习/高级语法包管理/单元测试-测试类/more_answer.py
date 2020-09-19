from survey import AnonymousSurvey

question = "what languages did you study?"
my_servey = AnonymousSurvey(question)
#more_question = []

my_servey.show_question()

while True:
    more_question = []
    while True:
        print("Enter 'q' at any time to quit!")
        response = input("Language:")
        if response == 'q':
            break
        more_question.append(response)
    my_servey.store_response(more_question)
    x = input("Next person: Enter 'q' to quit,and any key to continue!")
    if  x == 'q':
        break
my_servey.show_results()




