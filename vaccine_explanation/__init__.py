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
    age = models.IntegerField(label='年齢は何歳ですか？[デバッグ用]', min=13, max=125)
    gender = models.StringField(
        choices=[['男性', '男性'], ['女性', '女性']],
        label='性別は？[デバッグ用]',
        widget=widgets.RadioSelect,
    )
    name = models.StringField(label='あなたの氏名をフルネームでお書きください。')
    studentNumber = models.StringField(label='あなたの学籍番号をお書きください。')
    email = models.StringField(label='あなたの電子メールアドレスをお書きください。なお、大学から与えられている公式アカウントのものをご記入ください。それ以外のものを記入した場合、謝金は支払われません。')
    studentNumberTest = models.IntegerField(label='あなたの学籍番号をお書きください。(b,gを除き半角数字で入力してください)', min=1000000, max=2200000)
    q2_1 = models.StringField(
        choices=[['yes', 'はい、わかりやすかったです'], ['no', 'いいえ、わかりにくいところがありました']],
        label='先ほどの実験説明は理解しやすいものでしたか？',
        widget=widgets.RadioSelect,
    )
    q2_2 = models.StringField(label='今後の参考のためによろしければ、改善点等書いていただけるとありがたいです。(特になければ「特になし」とご記入ください)')
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
class ResearchExplanation(Page):
    form_model = 'player'

page_sequence = [ResearchExplanation]
