from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'vaccine_explanation'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    temp = models.StringField(label='temp')

# FUNCTIONS
# PAGES
class ResearchExplanation(Page):
    form_model = 'player'
    form_fields = ['temp']

page_sequence = [ResearchExplanation]
