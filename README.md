# Mermin-Peres-Magic-Square
[![License](https://img.shields.io/github/license/Qiskit/qiskit.svg?)](https://opensource.org/licenses/Apache-2.0)

## Overview 

This repository contains the python scripts used to perform the six measurements in the Mermin-Peres Magic Square on IBM's quantum computers using the `qiskit` library. 

## Usage

In order to use the code in this repository the `qiskit` library must be installed. The best way to do this is using `pip`:

```bash
$ pip install qiskit
```

See the [Official README](https://github.com/Qiskit/qiskit/blob/master/README.md) for general instructions or 
the [Installing Qiskit](https://github.com/Qiskit/qiskit/blob/master/docs/install.rst) page for a more detailed installation guide. 

Furthermore an IBM Quantum Experience account is required in order to configure an API key in order to send jobs to IBM Q systems. This is also explained in the [Installing Qiskit](https://github.com/Qiskit/qiskit/blob/master/docs/install.rst) page.

Once these prerequisites have been completed this repository may be cloned and the scripts may be used in order to perform the measurements in the Mermin-Peres Magic Square.

## Documentation 

The documentation of the methods used in the scrips is [here](code/Documentation.md).

## Authors and Citation
Altay Dikme and Nicolas Reichel are the authors of the scripts in this repository. Furthermore [Gunnar Björk](https://www.kth.se/profile/gbjork) and Amine Laghaout
are also authors of the paper using the results from these measurements (Titled: Measuring the Mermin-Peres magic square using an online quantum computer).
If you use these scripts, please cite us. If you wish to site the paper please use the following [BibTeX file](Cite.bib).

Furthermore when using qiskit, please cite the authors of the library as per [Qiskit's BibTeX file](https://github.com/Qiskit/qiskit/blob/master/Qiskit.bib).

## License 
[Apache License 2.0](LICENSE)
