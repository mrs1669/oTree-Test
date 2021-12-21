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
    isConsent = models.StringField(
        choices=[['agree', '同意する'], ['disagree', '同意しない']],
        label='',
        widget=widgets.RadioSelect,
    )

# FUNCTIONS
# PAGES
class ResearchExplanation(Page):
    form_model = 'player'

page_sequence = [ResearchExplanation]
