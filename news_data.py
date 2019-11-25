from newsapi import NewsApiClient
from Date import Date
from datetime import date
import matplotlib.pyplot as plt


plotDate = Date()

newsapi = NewsApiClient(api_key='2d819fc6a46d4f6aac483f8daf986949')

x_axis = [x for x in range(1, plotDate.day + 1)]
categories = []
categoriesAPI = []
y_axis = []

print('Enter categories:')
while True:
    string = input('')

    if string == '0':
        break

    categories.append(string)
    y_axis.append([])

for x in range(0, len(x_axis)):
    for y, count in zip(categories, range(0, len(categories))):
        print(plotDate.toString())
        categoriesAPI.append(newsapi.get_everything(q=y, from_param=plotDate.toString(), language='en'))
        y_axis[count].append(categoriesAPI[count]['totalResults'])

    categoriesAPI = []

    plotDate.substractDay(1)

legend = [label for label in categories]

for count in range(0, len(categories)):
    plt.scatter(x_axis, y_axis[count])

plt.legend(legend)    
plt.show()
