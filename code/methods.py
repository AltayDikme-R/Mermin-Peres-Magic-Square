# coding=UTF-8
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit import IBMQ
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor, backend_monitor, backend_overview
from qiskit.tools.visualization import plot_histogram, plot_bloch_vector

# *****************************************************************************
### Algorithms for each Row and Column in MP Square
## XⓍ1 - 1ⓍX - XⓍX measurement
def row1(qc, q_0, q_1, q_meas):
    qc.h(q_0)
    qc.h(q_1)

    qc.cx(q_0,q_meas)
    qc.cx(q_1,q_meas)

    qc.cx(q_0,q_meas)
    qc.cx(q_1,q_meas)

## 1ⓍY - YⓍ1 - YⓍY measurement (simplified)
def row2(qc, q_0, q_1, q_meas):
    qc.u2(0, np.pi/2, q_0)

    qc.u2(0, np.pi/2, q_1)

    qc.cx(q_0, q_meas)
    qc.cx(q_1, q_meas)

    qc.cx(q_0, q_meas)
    qc.cx(q_1, q_meas)

## XⓍY - YⓍX - ZⓍZ measurement
def row3(qc, q_0, q_1, q_meas):
    qc.cx(q_1,q_meas)
    qc.cx(q_0,q_meas)

    qc.h(q_0)
    qc.u2(0, np.pi/2, q_1)


    qc.cx(q_1, q_meas)
    qc.cx(q_0, q_meas)

    qc.u2(np.pi/2, 3*np.pi/2, q_0)

    qc.u2(3*np.pi/2, np.pi/2, q_1)

    qc.cx(q_1, q_meas)
    qc.cx(q_0, q_meas)

## XⓍ1 - 1ⓍY - XⓍY measurement
def col1(qc, q_0, q_1, q_meas):

    qc.h(q_0)

    qc.u2(0, np.pi/2, q_1)

    qc.cx(q_0, q_meas)
    qc.cx(q_1, q_meas)
    qc.cx(q_0, q_meas)
    qc.cx(q_1, q_meas)

## 1ⓍX - YⓍ1 - YⓍX measurement
def col2(qc, q_0, q_1, q_meas):

    qc.u2(0, np.pi/2, q_0)

    qc.h(q_1)

    qc.cx(q_0, q_meas)
    qc.cx(q_1, q_meas)
    qc.cx(q_0, q_meas)
    qc.cx(q_1, q_meas)


## XⓍX - YⓍY - ZⓍZ measurement
def col3(qc, q_0, q_1, q_meas):
    qc.cx(q_0, q_meas)
    qc.cx(q_1, q_meas)

    qc.h(q_0)
    qc.h(q_1)

    qc.cx(q_0,q_meas)
    qc.cx(q_1,q_meas)

    qc.u2(np.pi/2, 3*np.pi/2, q_0)
    qc.u2(np.pi/2, 3*np.pi/2, q_1)

    qc.cx(q_0,q_meas)
    qc.cx(q_1,q_meas)

# *****************************************************************************
# Functions for initializing different states
def xxinit(qc, q_0, q_1, q_meas):
    qc.h(q_0)
    qc.h(q_1)

def xyinit(qc, q_0, q_1, q_meas):
    qc.h(q_0)
    qc.h(q_1)
    qc.s(q_1)

def yxinit(qc, q_0, q_1, q_meas):
    qc.h(q_0)
    qc.h(q_1)
    qc.s(q_0)

def yyinit(qc, q_0, q_1, q_meas):
    qc.h(q_0)
    qc.h(q_1)
    qc.s(q_0)
    qc.s(q_1)

def zxinit(qc, q_0, q_1, q_meas):
    qc.h(q_1)

def zyinit(qc, q_0, q_1, q_meas):
    qc.h(q_1)
    qc.s(q_1)

def xzinit(qc, q_0, q_1, q_meas):
    qc.h(q_0)

def yzinit(qc, q_0, q_1, q_meas):
    qc.h(q_0)
    qc.s(q_0)

def zyinit(qc, q_0, q_1, q_meas):
    qc.h(q_1)
    qc.s(q_1)

def negzzinit(qc,q_0,q_1,q_meas):
    qc.x(q_0)
    qc.x(q_1)


# *****************************************************************************
# INDIVIDUAL OPERATION MEASUREMENTS
def meas_11_12(qc, q_0, q_1, q_meas):
    qc.h(q_0)
    qc.cx(q_0,q_meas)
    qc.cx(q_1,q_meas)

def meas_13(qc, q_0, q_1, q_meas):
    qc.h(q_0)
    qc.h(q_1)
    qc.cx(q_0,q_meas)
    qc.cx(q_1,q_meas)

def meas_21_22(qc, q_0, q_1, q_meas):
    qc.u2(0, np.pi/2, q_0)
    qc.cx(q_0,q_meas)
    qc.cx(q_1,q_meas)

def meas_23(qc, q_0, q_1, q_meas):
    qc.u2(0, np.pi/2, q_0)
    qc.u2(0, np.pi/2, q_1)
    qc.cx(q_0,q_meas)
    qc.cx(q_1,q_meas)

def meas_31(qc, q_0, q_1, q_meas):
    qc.h(q_0)
    qc.u2(0, np.pi/2, q_1)
    qc.cx(q_0, q_meas)
    qc.cx(q_1,q_meas)

def meas_32(qc, q_0, q_1, q_meas):
    qc.u2(0, np.pi/2, q_0)
    qc.h(q_1)
    qc.cx(q_0, q_meas)
    qc.cx(q_1, q_meas)

def meas_33(qc, q_0, q_1, q_meas):
    qc.cx(q_0, q_meas)
    qc.cx(q_1, q_meas)

# *****************************************************************************
# ROW AND COLUMN MEASUREMENTS WITH THREE ANCILLA QUBITS

def meas2_row1(qc, q_0, q_1, q_meas1, q_meas2, q_meas3):
    qc.h(q_0)
    qc.h(q_1)

    qc.cx(q_0, q_meas1)
    qc.cx(q_0, q_meas2)
    qc.cx(q_1, q_meas2)

    qc.measure(q_1, c[0])
    qc.measure(q_meas1, c[1])
    qc.measure(q_meas2, c[2])

def meas2_row2(qc, q_0, q_1, q_meas1, q_meas2, q_meas3):
    qc.u2(0, np.pi/2, q_0)
    qc.u2(0, np.pi/2, q_1)

    qc.cx(q_0, q_meas1)
    qc.cx(q_0, q_meas2)
    qc.cx(q_1, q_meas2)

    qc.measure(q_1, c[0])
    qc.measure(q_meas1, c[1])
    qc.measure(q_meas2, c[2])

def meas2_row3(qc, q_0, q_1, q_meas1, q_meas2, q_meas3):
    qc.cx(q_1,q_meas1)
    qc.cx(q_0,q_meas1)

    qc.h(q_0)
    qc.u2(0, np.pi/2, q_1)


    qc.cx(q_1, q_meas2)
    qc.cx(q_0, q_meas2)

    qc.u2(np.pi/2, 3*np.pi/2, q_0)
    qc.u2(3*np.pi/2, np.pi/2, q_1)

    qc.cx(q_1, q_meas3)
    qc.cx(q_0, q_meas3)

    qc.measure(q_meas1, c[0])
    qc.measure(q_meas2, c[1])
    qc.measure(q_meas3, c[2])

def meas2_col1(qc, q_0, q_1, q_meas1, q_meas2, q_meas3):
    qc.h(q_0)
    qc.u2(0, np.pi/2, q_1)

    qc.cx(q_0, q_meas1)
    qc.cx(q_0, q_meas2)
    qc.cx(q_1, q_meas2)

    qc.measure(q_1, c[0])
    qc.measure(q_meas1, c[1])
    qc.measure(q_meas2, c[2])

def meas2_col2(qc, q_0, q_1, q_meas1, q_meas2, q_meas3):
    qc.u2(0, np.pi/2, q_0)
    qc.h(q_1)

    qc.cx(q_0, q_meas1)
    qc.cx(q_0, q_meas2)
    qc.cx(q_1, q_meas2)

    qc.measure(q_1, c[0])
    qc.measure(q_meas1, c[1])
    qc.measure(q_meas2, c[2])

def meas2_col3(qc, q_0, q_1, q_meas1, q_meas2, q_meas3):
    qc.cx(q_0, q_meas1)
    qc.cx(q_1, q_meas1)

    qc.h(q_0)
    qc.h(q_1)

    qc.cx(q_0,q_meas2)
    qc.cx(q_1,q_meas2)

    qc.u2(np.pi/2, 3*np.pi/2, q_0)
    qc.u2(np.pi/2, 3*np.pi/2, q_1)

    qc.cx(q_0,q_meas3)
    qc.cx(q_1,q_meas3)
