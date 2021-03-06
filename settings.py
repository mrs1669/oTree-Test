from os import environ


SESSION_CONFIGS = [
    dict(
        name='survey',
        display_name="サンプル調査",
        app_sequence=['survey', 'payment_info'], 
        num_demo_participants=3,
    ),
    dict(
        name='prisoner',
        display_name="囚人のジレンマ",
        app_sequence=['prisoner', 'payment_info'], 
        num_demo_participants=2
    ),
    dict(
        name='vaccine',
        display_name="ワクチン接種",
        app_sequence=['research_intro', 'vaccine_explanation', 'vaccine', 'after_research_question', 'payment_info'], 
        num_demo_participants=3
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
oTreeの実験用プロジェクトを一覧表示しています。
"""


SECRET_KEY = '4431490396206'

INSTALLED_APPS = ['otree']
