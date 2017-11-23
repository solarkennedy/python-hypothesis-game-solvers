from hypothesis import note, settings
from hypothesis.stateful import RuleBasedStateMachine, rule, invariant


class GearWallProblem(RuleBasedStateMachine):
    ring1 = 180
    ring2 = 0
    ring3 = 45
    ring4 = 270
    desired_end_state = 90

    @rule()
    def mode1_right(self):
        self.ring1 = (self.ring1 + 45) % 360
        self.ring3 = (self.ring3 + 45) % 360

    @rule()
    def mode2_right(self):
        self.ring2 = (self.ring2 + 45) % 360
        self.ring4 = (self.ring4 + 45) % 360

    @rule()
    def mode3_right(self):
        self.ring3 = (self.ring3 + 45) % 360

    @rule()
    def mode4_right(self):
        self.ring1 = (self.ring1 + 45) % 360
        self.ring4 = (self.ring4 + 45) % 360

    @invariant()
    def not_solved(self):
        note("> Rings are {}, {}, {}, {}".format(self.ring1, self.ring2, self.ring3, self.ring4))
        assert not self.ring1 == self.ring2 == self.ring3 == self.ring4 == self.desired_end_state


with settings(max_examples=20000, stateful_step_count=20):
    GearWallTest = GearWallProblem.TestCase
