from survey import AnonymousSurvey

# Defining question and making a survey.
question = "What is your native language?"
my_survey = AnonymousSurvey(question)

# Displaying question and storing ansvers.
my_survey.show_question()
print("Insert 'q' to quit the program.\n")

while True:
    response = input("language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Displaying survey results.
print("\nWe thank each respondent for participating in the survey.")
my_survey.show_results()
