## Index

|                     Measurement Methods                 |
|:---------------------------------------------------:|
|              row1(qc, q_0, q_1, q_meas)             |
|              row2(qc, q_0, q_1, q_meas)             |
|              row3(qc, q_0, q_1, q_meas)             |
|              col1(qc, q_0, q_1, q_meas)             |
|              col2(qc, q_0, q_1, q_meas)             |
|              col3(qc, q_0, q_1, q_meas)             |
|                                                     |
|           meas_11_12(qc, q_0, q_1, q_meas)          |
|            meas_13(qc, q_0, q_1, q_meas)            |
|           meas_21_22(qc, q_0, q_1, q_meas)          |
|            meas_23(qc, q_0, q_1, q_meas)            |
|            meas_31(qc, q_0, q_1, q_meas)            |
|            meas_32(qc, q_0, q_1, q_meas)            |
|            meas_33(qc, q_0, q_1, q_meas)            |
|                                                     |
| meas2_row1(qc, q_0, q_1, q_meas1, q_meas2, q_meas3) |
| meas2_row2(qc, q_0, q_1, q_meas1, q_meas2, q_meas3) |
| meas2_row3(qc, q_0, q_1, q_meas1, q_meas2, q_meas3) |
| meas2_col1(qc, q_0, q_1, q_meas1, q_meas2, q_meas3) |
| meas2_col2(qc, q_0, q_1, q_meas1, q_meas2, q_meas3) |
| meas2_col3(qc, q_0, q_1, q_meas1, q_meas2, q_meas3) |

------
| Initialization Methods                                    |
|------------------------------------------------------|
| xxinit(qc, q_0, q_1, q_meas)                         |
| xyinit(qc, q_0, q_1, q_meas)                         |
| yxinit(qc, q_0, q_1, q_meas)                         |
| yyinit(qc, q_0, q_1, q_meas)                         |
| zxinit(qc, q_0, q_1, q_meas)                         |
| xzinit(qc, q_0, q_1, q_meas)                         |
| yzinit(qc, q_0, q_1, q_meas)                         |
| zyinit(qc, q_0, q_1, q_meas)                                                     |
| negzzinit(qc, q_0, q_1, q_meas)                                                      |
 
 
#### Measurement Methods

The first 13 measurement methods take 4 arguments, these are `qc`, `q_0`, `q_1`, and `q_meas`. `qc` is the quantum circuit object, and `q_0`,`q_1`,`q_meas` are qubits. Each method corresponds to a quantum circuit which can be easily discerned by the name of the method, e.g the row1 method corresponds to the quantum circuit for the first row in Mermin-Peres Magic Square and so on. meas_11_12 means that the method can be used for the first measurement in the first row and the second measurement in the first row thus reducing redundancy. 

The final 6 measurement methods take 6 arguments. As the previous methods the first argument `qc` is the quantum circuit object and the remaining arguments are qubits to be used. These methods require five qubits as we require three ancilla qubits for the measurements. 
