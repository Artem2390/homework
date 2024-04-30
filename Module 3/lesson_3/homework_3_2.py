class English:
    def greeting(self):
        return "Hello! How are you?"


class Spanish:
    def greeting(self):
        return "¡Hola! ¿Cómo estás?"


def hello_friend(lang1, lang2):
    print("Friend 1 (English):", lang1.greeting())
    print("Friend 2 (Spanish):", lang2.greeting())


english_friend = English()
spanish_friend = Spanish()

hello_friend(english_friend, spanish_friend)
