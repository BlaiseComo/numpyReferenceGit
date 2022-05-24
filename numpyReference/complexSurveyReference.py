import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = len(np.array(survey_responses)[np.array(survey_responses) == 'Ceballos'])
print(total_ceballos)

percentage_ceballos = (float(total_ceballos) / len(survey_responses))
print(percentage_ceballos)

possible_surveys = np.random.binomial(len(survey_responses), .54, size=10000) / float(len(survey_responses))

plt.hist(possible_surveys, range = (0,1), bins = 20)
plt.show()

ceballos_loss_surveys = np.mean(possible_surveys < 0.5)
print(ceballos_loss_surveys)

large_survey = np.random.binomial(float(7000), .54, size=10000) / float(7000)

incorrect_predictions = len(large_survey[large_survey < .5])

ceballos_loss_new = incorrect_predictions / float(7000)

print(ceballos_loss_new)


