# HTML — это язык разметки, используемый для определения структуры веб-страниц, посещаемых пользователями. HTML предоставляет средства для создания заголовков, абзацев, ссылок, цитат и других элементов. Каждый HTML-элемент обозначается открывающим и закрывающим тегами:
# <p>Если в ходе теста нет угрозы жизни, разве это вообще наука?</p>
# Теги заключаются в угловые скобки. Они определяют, где элемент начинается и где он заканчивается. Единственным различием между открывающим и закрывающим тегами является косая черта, которая предшествует имени тега.
# Открывающий и закрывающий теги, а также заключенное в них содержимое, могут располагаться как на одной строке (пример выше), так и на разных. Если теги и содержимое располагаются на разных строках, то сперва указывается открывающий тег, затем на следующий строке с отступом в два пробела указывается содержимое, а после на следующей строке указывается закрывающий тег, который располагается на том же уровне отступов, что и открывающий тег:
# <p>
#   Наука не решает вопрос Почему?, она решает вопрос А почему бы и нет?
# </p>
# Реализуйте класс HtmlTag. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
#     tag — HTML тег
#     inline — булево значение, по умолчанию равняется False
# Экземпляр класса HtmlTag должен являться реентерабельным контекстным менеджером, который позволяет генерировать HTML-код с правильными отступами и глубиной вложенности тегов. Параметр inline должен определять положение тегов и их содержимого. Если он имеет значение True, теги и содержимое должны располагаться на одной строке, если False — на разных строках.
# Класс HtmlTag должен иметь один метод экземпляра:
#     print() — метод, принимающий в качестве аргумента содержимое тега и выводящий его в рамках этого тега
# Примечание 1. Наглядные примеры использования класса HtmlTag продемонстрированы в тестовых данных.
# Примечание 2. В качестве отступов для каждого уровня используйте два пробела.
# Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
# Примечание 4. Класс HtmlTag должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.

class HtmlTag:
    count = -2
    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline
        self.tab = ' '

    def print(self, text):
        if self.inline:
            print(f"{HtmlTag.count * self.tab}<{self.tag}>{text}</{self.tag}>")
        else:
            print(f"{self.tab * HtmlTag.count + '  '}{text}")

    def __enter__(self):
        HtmlTag.count += 2
        if self.inline:
            return self
        else:
            print(f"{self.tab * HtmlTag.count}<{self.tag}>")
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.inline:
            HtmlTag.count -= 2
            return False
        else:
            print(f"{self.tab * HtmlTag.count}</{self.tag}>")
            HtmlTag.count -= 2
            return False

