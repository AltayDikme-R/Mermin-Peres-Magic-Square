# This script is used to measure each individual measurement in a row/column of the Mermin-Peres Magic Square.
# The script performs one measurement per run where the ancilla qubit (q_2) is measured at the end of the script.
# In order to perform all 9 measurements the program must be run 
# 9 times individually, by uncommenting whichever measurement the user wishes to perform (lines 23-31).

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
# INDIVIUAL MEASUREMENTS.

#meas_11_12(qc,q[0],q[1],q[2])
#meas_11_12(qc, q[1],q[0],q[2])
#meas_13(qc,q[0],q[1],q[2])
#meas_21_22(qc,q[1],q[0],q[2])
#meas_21_22(qc,q[0],q[1],q[2])
#meas_23(qc,q[0],q[1],q[2])
#meas_31(qc,q[0],q[1],q[2])
#meas_32(qc,q[0],q[1],q[2])
#meas_33(qc,q[0],q[1],q[2])

print(qc)

# Measure the ancilla qubit
#qc.measure(q[2],c[0])


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
