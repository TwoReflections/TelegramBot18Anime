import random
import URLs

token = "1268709960:AAFanrVm54FbLoNccGcrOkf1FFgFS8GqdOk"

Welcomers = ['Привет', 'Приветик', 'Приветики', 'Приветулечки', 'Ась?', 'Хаюшки', 'Кониттива', 'Доброго времени суток', 'Велкам']
Mood = ['Хорошо', 'Могло быть и лучше', 'Неплохо, если так подумать']
RandPic = URLs.img1

random1 = lambda: random.choice(Welcomers)
random2 = lambda: random.choice(Mood)
random3 = lambda: random.choice(RandPic)