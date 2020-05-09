#!/usr/bin/env python3
import unittest
from hypothesis import note, settings
from hypothesis.stateful import RuleBasedStateMachine, rule, invariant, precondition


class LeverProblem(RuleBasedStateMachine):
    total = 0
    nsteps = 0

    @rule()
    def west(self):
        self.total = self.total + 55
        self.nsteps = self.nsteps + 1

    @rule()
    def south(self):
        self.total = self.total + 40
        self.nsteps = self.nsteps + 1

    @precondition(lambda self: self.total >= 57)
    @rule()
    def north(self):
        self.total = self.total - 57
        self.nsteps = self.nsteps + 1

    @rule()
    def east(self):
        self.total = self.total + 40
        self.nsteps = self.nsteps + 1

    @invariant()
    def the_rules(self):
        assert 0 <= self.total <= 97
        assert self.nsteps <= 5

    @invariant()
    def not_solved(self):
        note("> total is: {s}".format(s=self.total))
        assert self.total != 88


QProblemTest = LeverProblem.TestCase
QProblemTest.settings = settings(max_examples=2000000)

if __name__ == "__main__":
    unittest.main()
