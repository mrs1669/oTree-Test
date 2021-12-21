from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'after_research_question'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(label='あなたの氏名をフルネームでお書きください。')
    studentNumber = models.StringField(label='あなたの学籍番号をお書きください。')
    email = models.StringField(label='あなたの電子メールアドレスをお書きください。なお、大学から与えられている公式アカウントのものをご記入ください。それ以外のものを記入した場合、謝金は支払われません。')


# FUNCTIONS
# PAGES

class AfterResearchQuestion(Page):
    form_model = 'player'
    form_fields = ['name','studentNumber','email']

page_sequence = [AfterResearchQuestion]
