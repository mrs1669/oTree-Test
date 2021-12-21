from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'vaccine'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    isConsent = models.StringField(
        choices=[['agree', '同意する'], ['disagree', '同意しない']],
        label='',
        widget=widgets.RadioSelect,
    )
    name = models.StringField(label='あなたの氏名をフルネームでお書きください。')
    studentNumber = models.StringField(label='あなたの学籍番号をお書きください。')
    email = models.StringField(label='あなたの電子メールアドレスをお書きください。なお、大学から与えられている公式アカウントのものをご記入ください。それ以外のものを記入した場合、謝金は支払われません。')

# FUNCTIONS
# PAGES
class BasicInformation(Page):
    form_model = 'player'
    form_fields = ['name','studentNumber','email']

class Introduction(Page):
    form_model = 'player'
    form_fields = ['isConsent']

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['isConsent'] == 'disagree':
            return '同意していただけない場合は実験に進むことはできません。ブラウザを閉じて実験を終了してください。'

page_sequence = [Introduction, BasicInformation]
