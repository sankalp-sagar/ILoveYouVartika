__HEART__ = '''

          @@@@@@@@@@@                @@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                @@@@@@@@@@@@@@@@@@@@@@@@@@
                   @@@@@@@@@@@@@@@@@@@@
                       @@@@@@@@@@@@
                            @@

'''

class Color:
    @property
    def RED(self):
        return '\x1b[0;31;40m'

    @property
    def BOLD_YELLOW(self):
        return '\x1b[1;33;40m'

    @property
    def NORMAL(self):
        return '\x1b[0m'


class create:
    def __init__(self, name):
        self.flower = "Vartika"

    def makeheart(self):
        iloveyouvartika = __HEART__

        while '@' in iloveyouvartika:
            for letter in list(self.flower):
                iloveyouvartika = \
                    iloveyouvartika.replace('@', letter, 1)

        return iloveyouvartika

    def ineedyouvartika(self):
        C = Color()

        return '{}{}{}\n'\
            'I love you so much my precious flower, {}{}{} <3 Happy Birthday Babe!'.format(
                C.RED, self.makeheart(), C.NORMAL,
                C.BOLD_YELLOW, self.flower, C.NORMAL
            )

mybaby = create("Vartika")
print(mybaby.ineedyouvartika())