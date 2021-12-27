from otree.api import *
import random


class Constants(BaseConstants):
    name_in_url = 'vaccine'
    players_per_group = None
    num_rounds = random.randint(4,9)
    instruction_template = 'vaccine/instruction.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    cooperate = models.BooleanField(
        choices=[[True, '先着順方式'], [False, '抽選一括方式']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    main = models.StringField(label='実験のメイン')
    receive_place = models.StringField(
        choices=[['choice_x', '受取所 X'], ['choice_y', '受取所 Y']],
        label='行きたい受取所を選択してください',
        widget=widgets.RadioSelect,
    )


# FUNCTIONS
# PAGES
class Choose(Page):
    form_model = 'player'
    form_fields = ['cooperate']

class MainResearch(Page):
    form_model = 'player'
    form_fields = ['receive_place']

page_sequence = [Choose, MainResearch]
