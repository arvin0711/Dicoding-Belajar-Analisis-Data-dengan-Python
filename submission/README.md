Setup environment
conda create --name main-ds python=3.11.0
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel

Run steamlit app
streamlit run dashboard.py
