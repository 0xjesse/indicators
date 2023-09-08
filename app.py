import os
import subprocess

from flask import Flask, render_template

app = Flask(__name__)

def get_ticker_data():
    # Run the price.py script and capture its output
    result = subprocess.run(['python', 'price.py'], capture_output=True, text=True)
    ticker_data = result.stdout.strip().split('\n')
    return ticker_data

@app.route('/')
def index():
    # Get ticker data
    ticker_data = get_ticker_data()

    # Run the rsi.py script and capture its output
    result_rsi = subprocess.run(['python', 'rsi.py'], capture_output=True, text=True)
    rsi_output = result_rsi.stdout
    
        # Run the macd2.py script and capture its output
    result_macd = subprocess.run(['python', 'macd2.py'], capture_output=True, text=True)
    macd_output = result_macd.stdout

    # Construct the absolute path to the styled_output.html file
    styled_output_path = os.path.join(app.root_path, 'styled_output.html')

    # Read the styled DataFrame HTML file
    with open(styled_output_path, 'r') as f:
        styled_df_html = f.read()
        
     # Construct the absolute path to the styled_macd_data.html file (for MACD)
    styled_macd_output_path = os.path.join(app.root_path, 'styled_macd_data.html')
    
    # Read the styled MACD DataFrame HTML file (for MACD)
    with open(styled_macd_output_path, 'r') as f:
        styled_macd_df_html = f.read()    

    return render_template('index.html', ticker_data=ticker_data, rsi_output=rsi_output, styled_df_html=styled_df_html, styled_macd_df_html=styled_macd_df_html, macd_output=macd_output)


if __name__ == '__main__':
    app.run(debug=True)
    
    
    