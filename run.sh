#!/bin/bash
source ~/opt/anaconda3/etc/profile.d/conda.sh
conda activate webapp

echo webapp env activate

streamlit run main.py
