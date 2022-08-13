import googletrans


class Translate:
    def __init__(self, text,language):
        self.text = text
        self.language = language
        self.translated_text = []

    def get_translate(self):
        translator = googletrans.Translator()
        self.translated_text = translator.translate(self.text, dest=self.language)
        return self.translated_text.text
