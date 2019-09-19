import strawberryfields as sf
from strawberryfields.ops import *
from strawberryfields.utils import scale
from numpy import pi, sqrt

prog = sf.Program(3)


@sf.convert
def custom(x):
    return -x * sqrt(2)


with prog.context as q:
    # prepare initial states
    Coherent(1 + 0.5j) | q[0]
    Squeezed(-2) | q[1]
    Squeezed(2) | q[2]

    # apply gates
    BS = BSgate(pi / 4, pi)
    BS | (q[1], q[2])
    BS | (q[0], q[1])

    # perform homodyne measurements
    MeasureX | q[0]
    MeasureP | q[1]

    # Displacement gates conditioned on the measurement
    Xgate(scale(q[0], sqrt(2))) | q[2]
    Zgate(custom(q[1])) | q[2]

eng = sf.Engine('fock', backend_options={"cutoff_dim": 15})
result = eng.run(prog, run_options={
                 "shots": 1, "modes": None}, compile_options={})
print(result.samples)
print(result.state)
state = result.state
print(state.dm().shape)
