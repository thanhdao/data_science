# assignment8.py
import matplotlib.pyplot as plt
import pandas as pd

from random import *
import numpy as np

def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


data_frame = pd.read_csv('data_2.csv')
headers = data_frame.columns.values
print(headers)

data = data_frame.values
print(data)
print(data_frame.head)


years = headers[2:7]
print(years)
weather_conditions = data[range(1,21,3), 0]
print(weather_conditions)
consequenses = data[0:3,1]
print(consequenses)

no_of_accident = data[range(0,21,3),2:7]
print(no_of_accident)
no_of_death = data[range(1,21,3),2:7]
no_of_wounded = data[range(2,21,3),2:7]


width = 0.25  # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

total = data_frame[0:3]
print(total)
# total_data = np.array(total.iloc[0:, 2:]).astype(float)
total_data = total.iloc[0:, 2:].values
print(total_data)



indices = np.arange(len(years))
print(indices)

# Display Total Accident
# total_accident = total_data[0]
# total_death = total_data[1]
# total_wounded = total_data[2]

total_accident = no_of_accident[0]
total_death = no_of_death[0]
total_wounded = no_of_wounded[0]

# bar1 = ax.bar(indices - width, no_of_accident[0], width, color='b', align='center' )
# bar2 = ax.bar(indices, no_of_death[0], width, color='r', align='center' )
# bar3 = ax.bar(indices + width, no_of_wounded[0], width, color='g', align='center' )

# Display Accient by Rain
# bar1 = ax.bar(indices - width, no_of_accident[5], width, color='b', align='center' )
# bar2 = ax.bar(indices, no_of_death[5], width, color='r', align='center' )
# bar3 = ax.bar(indices + width, no_of_wounded[5], width, color='g', align='center' )


# ax.set_ylabel('Number')
# ax.set_title('Accidents by Snow')
# ax.set_xticks(indices+width)
# ax.set_xticklabels(years)
# ax.legend((bar1[0], bar2[0], bar3[0]), ('Accident', 'Death', 'Wound' ))

# autolabel(bar1)
# autolabel(bar2)
# autolabel(bar3)

# plt.show()

# Total accident by years
# plt.plot(years, no_of_accident[5])
# plt.plot(years, no_of_death[5])
# plt.plot(years, no_of_wounded[5])
# plt.title('Total accidents by snow')
# plt.xlabel('Years')
# plt.ylabel('Number')
# plt.legend(('Accident', 'Death', 'Wound' ))


# print(years)
# print(total_accident)
# plt.show()


data_2015 = data_frame[['Weather Condition', 'Base Year', '2015']]

data_2015_death = data_2015[1::3]
data_2015_death.head()
list = np.array(data_2015_death['2015'])
clear_per = (list[1] / list[0]) * 100
cloudy_per = (list[2] / list[0]) * 100
rain_per = (list[3] / list[0]) * 100
foggy_per = (list[4] / list[0]) * 100
snow_per = (list[5] / list[0]) * 100
other_per = (list[6] / list[0]) * 100
data_2015_weather = [clear_per, cloudy_per, rain_per, foggy_per, snow_per, other_per]
labels = ['Clear', 'Rain', 'Foggy', 'Snow', 'Cloudy', 'Other']
plt.pie(data_2015_weather, labels=labels, autopct="%0.2f")
plt.axes().set_aspect("equal")
plt.title('Accident by Weather 2015')
plt.show()