# Python Hypothesis Game Solvers

This repo has solutions to some games using [Python Hypothesis](https://hypothesis.readthedocs.io/en/latest/)

## [Quern - Undying Thoughts](http://querngame.com/)


### Gear Wall Mover

<a href="https://youtu.be/nUkXURNNGjo?t=2900" target="_blank">
<img src="https://raw.githubusercontent.com/solarkennedy/python-hypothesis-game-solvers/master/gear_wall_mover.png" width="480" height="270" border="10" />
</a>

Solver: [gear_wall_mover.py](https://github.com/solarkennedy/python-hypothesis-game-solvers/blob/master/gear_wall_mover.py)

This puzzle has 4 rings, but they don't move independently.
This solver asserts that there is no sequence of moves that result in all of the rings "pointing 90 degrees".

```
Falsifying example: run_state_machine(factory=GearWallProblem, data=data(...))
state = GearWallProblem()
> Rings are 180, 0, 45, 270
state.mode1_right()
> Rings are 225, 0, 90, 270
state.mode1_right()
> Rings are 270, 0, 135, 270
state.mode1_right()
> Rings are 315, 0, 180, 270
state.mode1_right()
> Rings are 0, 0, 225, 270
state.mode2_right()
> Rings are 0, 45, 225, 315
state.mode2_right()
> Rings are 0, 90, 225, 0
state.mode2_right()
> Rings are 0, 135, 225, 45
state.mode2_right()
> Rings are 0, 180, 225, 90
state.mode2_right()
> Rings are 0, 225, 225, 135
state.mode2_right()
> Rings are 0, 270, 225, 180
state.mode2_right()
> Rings are 0, 315, 225, 225
state.mode2_right()
> Rings are 0, 0, 225, 270
state.mode2_right()
> Rings are 0, 45, 225, 315
state.mode2_right()
> Rings are 0, 90, 225, 0
state.mode3_right()
> Rings are 0, 90, 270, 0
state.mode3_right()
> Rings are 0, 90, 315, 0
state.mode3_right()
> Rings are 0, 90, 0, 0
state.mode3_right()
> Rings are 0, 90, 45, 0
state.mode3_right()
> Rings are 0, 90, 90, 0
state.mode4_right()
> Rings are 45, 90, 90, 45
state.mode4_right()
> Rings are 90, 90, 90, 90
state.teardown()
```

### Lever Problem

### Mechanics Solver

<a href="https://youtu.be/nUkXURNNGjo?t=3136" target="_blank">
<img src="https://raw.githubusercontent.com/solarkennedy/python-hypothesis-game-solvers/master/mechanics_solver.png" width="480" height="270" border="10" />
</a>

Solver: [mechanics_solver.py](https://github.com/solarkennedy/python-hypothesis-game-solvers/blob/master/mechanics_solver.py)

```
Falsifying example: test_mechanics_solver(positions=[5, 4, 6, 2, 14])
```
