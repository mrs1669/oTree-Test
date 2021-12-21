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
    q2_1 = models.StringField(
        choices=[['yes', 'はい、わかりやすかったです'], ['no', 'いいえ、わかりにくいところがありました']],
        label='先ほどの実験説明は理解しやすいものでしたか？',
        widget=widgets.RadioSelect,
    )
    q2_2 = models.StringField(label='今後の参考のためによろしければ、改善点等書いていただけるとありがたいです。(特になければ「特になし」とご記入ください)')


# FUNCTIONS
# PAGES
class FF(Page):
    form_model = 'player'
    form_fields = ['q2_1','q2_2']

page_sequence = [FF]
