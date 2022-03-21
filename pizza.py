
import matplotlib.pyplot as pyplot

labels = ("Python", "java", "scala", "C#","Outros")
sizes = [30,30,15,10,15]

pyplot.pie(sizes,labels=labels,
 autopct="%1.f%%",
 counterclock=False,startangle=90)

pyplot.show()