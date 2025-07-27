# Generative AI for β-Peptide Design Targeting ABL1 Kinase

This repository presents a generative modeling framework for the design of β-peptides with predicted activity against ABL1 kinase. ABL1 is a well-established target in oncology, and β-peptides offer a promising therapeutic modality due to their enhanced stability, tunable side chains, and resistance to proteolysis. Our goal is to integrate generative deep learning with structure-based design and optimization to propose novel β-peptide sequences with potential kinase inhibitory activity.

The approach begins with sequence-conditioned deep generative models trained on known kinase-inhibitory peptides and β-peptide derivatives. Using a combination of recurrent neural networks and latent variable modeling, the system generates novel peptide sequences that obey the chemical constraints of β-amino acid frameworks. Generated candidates are then subjected to molecular docking pipelines against the ABL1 active site, and their structural compatibility is evaluated via scoring functions and conformational sampling.

The `model.py` script contains a prototype sequence generation model. It can be trained on peptide datasets and used to sample novel sequences, optionally guided by structure or motif constraints. The `data/` folder contains preliminary datasets used during experimentation, including a `test.csv` file with reference sequences. Future iterations will incorporate reinforcement learning (RL) or genetic optimization for feedback-guided generation, using docking or predicted bioactivity as reward signals.

This project serves as a foundation for generative peptide modeling in the context of kinase inhibition and is part of a broader exploration of AI-driven therapeutic design. The framework is modular and extensible to other protein targets and peptide classes, including α/β-hybrids and stapled peptides.

While preliminary, this work demonstrates the feasibility of combining sequence-based generation with target-specific optimization, bridging generative AI and modern medicinal chemistry.
