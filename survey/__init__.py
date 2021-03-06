from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='年齢は何歳ですか？[デバッグ用]', min=13, max=125)
    gender = models.StringField(
        choices=[['男性', '男性'], ['女性', '女性']],
        label='性別は？[デバッグ用]',
        widget=widgets.RadioSelect,
    )
    name = models.StringField(label='あなたの氏名をフルネームでお書きください。')
    studentNumber = models.IntegerField(label='あなたの学籍番号をお書きください。(b,gを除き半角数字で入力してください)', min=1000000, max=2200000)
    q2_1 = models.StringField(
        choices=[['yes', 'はい、わかりやすかったです'], ['no', 'いいえ、わかりにくいところがありました']],
        label='先ほどの実験の説明は理解しやすいものでしたか？',
        widget=widgets.RadioSelect,
    )
    crt_bat = models.IntegerField(
        label='''
        あんけ１'''
    )
    crt_widget = models.IntegerField(
        label='''
        あんけ２
        '''
    )
    crt_lake = models.IntegerField(
        label='''
        あんけ３
        '''
    )


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender','name','studentNumber']


class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget', 'crt_lake']

class FF(Page):
    form_model = 'player'
    form_fields = ['q2_1']


page_sequence = [Demographics, FF, CognitiveReflectionTest]
