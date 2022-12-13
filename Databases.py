import sqlite3 as sq


class QuizQuestions:
    def __init__(self):
        # connect to database file
        self.conn = sq.connect('database.db')
        self.c = self.conn.cursor()
        # init table
        self.createTable()
        self.clearTable()
        self.fillTable()
        self.currentList = []

    def createTable(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        level INTEGER NOT NULL,
        stage INTEGER NOT NULL
        );''')

    def clearTable(self):
        self.c.execute('''DELETE FROM tasks''')

    def fillTable(self):
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Qué', 'WHAT', 1, 1);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Quiero', 'I WANT', 1, 1);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Quieres', 'YOU WANT', 1 , 1);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Tomate', 'TOMATO', 1, 1);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Patata', 'POTATO', 1, 1);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Botella', 'BOTTLE', 1, 2);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Zumo', 'JUICE', 1, 2);''')
        self.c.execute(
            '''INSERT INTO tasks (question, answer, level, stage) VALUES ('Cuanto cuesta', 'HOW MUCH DOES IT COST', 1, 2);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Por favor', 'PLEASE', 1, 2);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('También', 'ALSO', 1, 2);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Carne', 'MEAT', 1, 3);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Verdura', 'VEGETABLE', 1, 3);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Sí', 'YES', 1, 3);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Grande', 'BIG', 1, 3);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Pequeño', 'SMALL', 1, 3);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Billete', 'TICKET', 2, 1);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Comprar', 'BUY', 2, 1);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Tren', 'TRAIN', 2, 1);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Autobus', 'BUS', 2, 1);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Puedo', 'I CAN', 2, 1);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Hora', 'HOUR', 2, 2);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Sale', 'IT LEAVES', 2, 2);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Decir', 'TELL', 2, 2);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Próximo', 'NEXT', 2, 2);''')
        self.c.execute(
            '''INSERT INTO tasks (question, answer, level, stage) VALUES ('Pagar en efectivo', 'PAY IN CASH', 2, 2);''')
        self.c.execute(
            '''INSERT INTO tasks (question, answer, level, stage) VALUES ('Lleva un retraso', 'IT IS DELAYED', 2, 3);''')
        self.c.execute(
            '''INSERT INTO tasks (question, answer, level, stage) VALUES ('De ida y vuelta', 'ROUND TRIP', 2, 3);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Vía', 'PLATFORM', 2, 3);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Pero', 'BUT', 2, 3);''')
        self.c.execute('''INSERT INTO tasks (question, answer, level, stage) VALUES ('Señor', 'SIR', 2, 3);''')
        self.conn.commit()

    def search(self, level, stage):
        for i in self.c.execute(f'''SELECT question, answer FROM tasks WHERE level={level} AND stage={stage}'''):
            self.currentList.append(i)
        return self.currentList

    def clearSearch(self):
        self.currentList = []


class Dialogue:
    def __init__(self):
        self.conn = sq.connect('database.db')
        self.c = self.conn.cursor()
        self.createTable()
        self.clearTable()
        self.fillTable()

    def createTable(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS dialogue (
        id INTEGER PRIMARY KEY,
        line TEXT NOT NULL,
        line2 TEXT,
        level INTEGER NOT NULL,
        stage INTEGER NOT NULL,
        last BOOL NOT NULL
        );''')

    def clearTable(self):
        self.c.execute('''DELETE FROM dialogue''')

    def fillTable(self):
        self.c.execute('''INSERT INTO dialogue (line, level, stage, last) VALUES ('Hello there!', 1, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, line2, level, stage, last) VALUES ('I am your teacher and I am going to help you master the basics of', 'Spanish quickly and easily without the pain.', 1, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, line2, level, stage, last) VALUES ('Remember that all words you are shown, whether they are just used as an', 'example or in a list, will come up later.', 1, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('To start off you should understand a bit about how Spanish differs from English.', 1, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, line2, level, stage, last) VALUES ('All articles (things like the or a), words, and adjectives can be either', 'feminine or masculine.', 1, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, line2, level, stage, last) VALUES ('Generally words ending in -o are masculine and -a are feminine, but there are', 'lots of exeptions.', 1, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('un - a (masculine), una - a (femenine), el - the (masculine), la - the (femenine)', 1, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, line2, level, stage, last) VALUES ('Another feature of Spanish is that it has accents, and they can change the', 'meaning of a word.', 1, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('for example: que - that, qué - what', 1, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, line2, level, stage, last) VALUES ('The infinitive (to do, to work, to eat) of verbs in Spanish all end in -r e.g.', 'querer - to want', 1, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('But they can change the person they are referring to based on their ending.', 1, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('quiero - I want, quieres - you want', 1, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('Here is a dialogue about shopping. ', 1, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('Try and follow it the best you can using the things you have been taught.', 1, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, line2, level, stage, last) VALUES ('There will be some words you have not been shown but that are very close', 'to English, so see if you can guess the meaning.', 1, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, line2, level, stage, last) VALUES ('Do not worry if you cannot this time though, because there will be an english', 'translation to follow along if you need.', 1, 1, 1);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('Here is some useful vocab that will come up in the following dialogue or that came up earlier.', 1, 2, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('hola - hello, buenos días - good day, también - also, y - and, botella - bottle', 1, 2, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('zumo - juice, agua - water, cuanto cuesta - how much does it cost?, por favor - please', 1, 2, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('Here is a short dialogue.', 1, 2, 1);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('Here is some useful vocab that will come up in the following dialogue or that came up earlier.', 1, 3, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('vale - ok, cincuenta - 50, cinco - 5, fruta - fruit, verdura - vegetable', 1, 3, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('carne - meat, grande - big, pequeño - small, tienes - you have', 1, 3, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('In Spanish adjectives agree with the noun much like the articles.', 1, 3, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('la carne - the meat, la carne pequeña - the small meat, el zumo - the juice', 1, 3, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('el zumo pequeño - the small juice, las botellas pequeñas - the small bottles', 1, 3, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('The adjective takes -a or -o if it is singular or -as or -os if it is plural apart from in the case of adjectives like grande', 1, 3, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('Try and spot the pattern.', 1, 3, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('el zumo grande - the big juice, la verdura grande - the big vegetable', 1, 3, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('los zumos grandes - the big juices, las verdura grandes - the big vegetable', 1, 3, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('adjectives ending in -e do not change depending on gender, only get an -s in plural', 1, 3, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('Here is a short dialogue.', 1, 3, 1);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('In Spanish to talk about movement you can use;', 2, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('a - to / at, para - to / in order to', 2, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('As well as querer anothe useful verb is poder;', 2, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('puedo - i can, puedes - you can', 2, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('Here is some useful vocab when you are using public transport', 2, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('billete - ticket, comprar - buy, tren - train, autobus - bus', 2, 1, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('This is a short dialogue about buying a ticket', 2, 1, 1);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('To talk about the time in Spanish we use, a la, for 1 o-clock, and, a las, for all other times, followed by the number', 2, 2, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('a las cinco - at 5 o-clock, a las dos - at 2 o-clock, a las diez - at 10 o-clock, a la una - at 1 o-clock', 2, 2, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('Here is some more vocab to talk about public transport;', 2, 2, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('hora - hour, a qué hora - at what time, sale - it leaves', 2, 2, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('decir - tell, próximo - next, pagar en efectivo - pay in cash', 2, 2, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('Here is a diologue using the vocab you just learnt;', 2, 2, 1);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('Here is some very useful vocab about transport;', 2, 3, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('lleva un retraso - it is delayed, de ida - one-way trip', 2, 3, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('de ida y vuelta - round trip (literally, go and return), vía - platform, pero - but', 2, 3, 0);''')
        self.c.execute(
            '''INSERT INTO dialogue (line, level, stage, last) VALUES ('This is a good example of a full dialogue that you might have at a train station', 2, 3, 1);''')
        self.conn.commit()

    def search(self, level, stage):
        result = []
        for i in self.c.execute(f'''SELECT line, line2 FROM dialogue WHERE level={level} AND stage={stage}'''):
            result.append(i)
        return result


class Transcript:
    def __init__(self):
        self.conn = sq.connect('database.db')
        self.c = self.conn.cursor()
        self.createTable()
        self.clearTable()
        self.fillTable()

    def createTable(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS transcript (
           id INTEGER PRIMARY KEY,
           line TEXT NOT NULL,
           level INTEGER NOT NULL,
           stage INTEGER NOT NULL,
           last BOOL NOT NULL,
           transcription TEXT NOT NULL
           );''')

    def clearTable(self):
        self.c.execute('''DELETE FROM transcript''')

    def fillTable(self):
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Hello', 1, 1, 0, 'Hola');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Good morning', 1, 1, 0, 'Buenos días');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('What do you want?', 1, 1, 0, 'Qué quieres?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('I want a kilo of potatoes', 1, 1, 0, 'Quiero un kilo de patatas');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('And?', 1, 1, 0, 'Y?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('I want a tomato as well', 1, 1, 1, 'Quiero un tomate también');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Good morning', 1, 2, 0, 'Buenos días');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Hello', 1, 2, 0, 'Hola');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('How much does a bottle of water cost?', 1, 2, 0, 'Cuanto cuesta una botella de agua?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('One euro ', 1, 2, 0, 'Un euro');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Hmmm... and a bottle of fruit juice?', 1, 2, 0, 'Hmmm... y una botella de zumo de fruta?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('1.50', 1, 2, 0, 'Un euro cincuenta');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('I want a bottle of water and a bottle of squash please', 1, 2, 0, 'Quiero una botella de agua y una botella de zumo de fruta también por favor');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('OK', 1, 2, 1, 'Vale');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Hello', 1, 3, 0, 'Hola');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Good morning', 1, 3, 0, 'Buenos días');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('What do you want?', 1, 3, 0, 'Qué quieres?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Do you have vegtables?', 1, 3, 0, 'Tienes verduras?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Yes', 1, 3, 0, 'Sí');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('How much does a big tomatoe cost?', 1, 3, 0, 'Cuanto cuesta un tomate grande?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('One euro', 1, 3, 0, 'Un euro');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('I want 5 big tomatoes', 1, 3, 0, 'Quiero cinco tomates grandes');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('And?', 1, 3, 0, 'Y?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Do you have fruit?', 1, 3, 0, 'Tienes fruta?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Yes', 1, 3, 0, 'Sí');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('I want a small melon', 1, 3, 0, 'Quiero un melón pequeño');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('And?', 1, 3, 0, 'Y?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Do you have meat?', 1, 3, 0, 'Tienes carne?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('No', 1, 3, 1, 'No');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Hello', 2, 1, 0, 'Hola');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Can I buy a ticket to Madrid?', 2, 1, 0, 'Puedo comprar un billete para Madrid?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Yes', 2, 1, 0, 'Sí');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('How much does it cost?', 2, 1, 0, 'Cuanto cuesta?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('5 euros', 2, 1, 1, 'Cinco euros');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Good morning', 2, 2, 0, 'Buenas días');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Can you tell me at what time the next bus to Valencia leaves?', 2, 2, 0, 'Puedes decirme a qué hora sale el próximo autobus para Valencia?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('It leaves at 2 o-clock', 2, 2, 0, 'Sale a las dos');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Thank you', 2, 2, 0, 'Muchas gracias');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Do you want to buy a ticket?', 2, 2, 0, 'Quires comprar un billete?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Yes, can I pay in cash?', 2, 2, 0, 'Sí, puedo pagar en efectivo?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Yes, you can', 2, 2, 1, 'Sí, puedes');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Hello, sir', 2, 3, 0, 'Hola, Señor');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Can you tell me at what time the next train to Barcelona leaves?', 2, 3, 0, 'Puedes decirme a qué hora sale el próximo tren para Barcelona?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('It leaves at 5 but it is delayed an hour', 2, 3, 0, 'Sale a las cinco, pero lleva un retraso de una hora');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Can I buy a ticket?', 2, 3, 0, 'Puedo comprar un billete?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('A round trip?', 2, 3, 0, 'De ida y vuelta?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('No, only a one-way', 2, 3, 0, 'No, solo de ida');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('It costs 10 euros', 2, 3, 0, 'Cuesta diez euros');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('What platform does it leave from?', 2, 3, 0, 'De qué vía sale?');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Platform 2', 2, 3, 0, 'Vía dos');''')
        self.c.execute(
            '''INSERT INTO transcript (line, level, stage, last, transcription) VALUES ('Thank you', 2, 3, 1, 'Muchas gracias');''')
        self.conn.commit()

    def search(self, level, stage):
        result = []
        for i in self.c.execute(
                f'''SELECT line, transcription, last FROM transcript WHERE level={level} AND stage={stage}'''):
            result.append(i)
        return result

# t = Transcript()
# print(t.search(1, 1))
#
# d = Dialogue()
# print(d.search(1, 1))
#
# Q = QuizQuestions()
# print(Q.search(1, 3))
