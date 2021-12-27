from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'vaccine'
    players_per_group = None
    num_rounds = 1
    instruction_template = 'vaccine/instruction.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    main = models.StringField(label='実験のメイン')


# FUNCTIONS
# PAGES
class MainResearch(Page):
    form_model = 'player'
    form_fields = ['main']

page_sequence = [MainResearch]
