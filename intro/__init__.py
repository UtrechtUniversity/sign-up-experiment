from otree.api import *


doc = """
Introduction to the experiment
"""


class C(BaseConstants):
    NAME_IN_URL = 'intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    participate = models.BooleanField(
        label="Do you want to participate in the study?",
        choices=[[True, "Yes"], [False, "No"]],
        widget=widgets.RadioSelect
    )

    time_slots = models.StringField(
        choices=[
            "12:00–13:00",
            "13:30–14:30",
            "15:00–16:00",
        ],
        label="Select the time slot you would like to participate in the study.\n"
              "Please make sure you are available at that time slot.",
        blank=True
    )

# PAGES
class Introduction(Page):
    pass


class Register(Page):
    form_model = 'player'
    form_fields = ['participate', 'time_slots']

    @staticmethod
    def error_message(player, values):
        if values['participate'] and not values['time_slots']:
            return "Please select a time slot if you want to participate."

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        participant.participate = player.participate
        participant.time_slots = player.time_slots


page_sequence = [Introduction, Register,]
