# This script is used to measure each individual row/column of the Mermin-Peres Magic Square.
# The script measures one row or column per run where the ancilla qubit (q_2) is measured at the end of the script.
# In order to measure all 6 row/columns the program must be run 6 times individually, by uncommenting whichever row/column the user wishes to measure (lines 19-24).

from methods import *

## Setup
# Load IBMQ account credentials
IBMQ.load_accounts()

# Create quantum register with 3 qubits
q = QuantumRegister(3,'q')

# Create a classical register with 1 bits (one bit is required for each row/column as you can only measure one time per run of the script)
c = ClassicalRegister(1)

# Create a quantum circuit acting on the q register
qc = QuantumCircuit(q,c)

# *****************************************************************************
# 'NORMAL' MEASUREMENTS. Only the ancilla qubit is measured at the end of the circuit

row1(qc,q[0],q[1],q[2])
#row2(qc,q[0],q[1],q[2])
#row3(qc,q[0],q[1],q[2])
#col1(qc,q[0],q[1],q[2])
#col2(qc,q[0],q[1],q[2])
#col3(qc,q[0],q[1],q[2])

print(qc)

# Measure the ancilla qubit
qc.measure(q[0],c[0])


# *****************************************************************************
# EXECUTION
# *****************************************************************************

backend = IBMQ.get_backend('ibmqx4')
# backend = IBMQ.get_backend('ibmqx2')
# backend = IBMQ.get_backend('ibmq_16_melbourne')
# backend = IBMQ.get_backend('ibmq_qasm_simulator')

print("Name: ", backend.name())

shots = 8192          # Number of shots to run the program (experiment); maximum is 8192 shots.
max_credits = 15      # Maximum number of credits to spend on executions.

# Execution
#Ask for user input before execution
# cont = input("Execute? y/n : ")
# if cont == 'n':
#     quit()
# else:
#     pass

#Create a job object
job_exp = execute(qc, backend=backend, shots=shots, max_credits=max_credits)
backend_monitor(backend)
job_monitor(job_exp)

# Results
result_exp = job_exp.result()
counts_exp = result_exp.get_counts(qc)
print(counts_exp)
