from matplotlib import pyplot
import numpy as np

languages = ('C', 'Java', 'Python', 'C++', 'C#', 'Visual Basic','JavaScript', 'PHP', 'R', 'SQL')
percent = [16.48, 12.53, 12.21, 6.91, 4.2, 3.92, 2.35, 2.12, 1.6, 1.53]

y = np.arange(len(languages))

pyplot.bar(y, percent)
pyplot.xticks(y, languages)
pyplot.xlabel('Język')
pyplot.ylabel('Popularność [%]')
pyplot.title('10 najpopularniejszych języków programowania')
pyplot.show()