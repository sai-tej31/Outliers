from flask import Flask, request, render_template
import pandas as pd
from utils import find_limits,treat_outliers
import matplotlib.pyplot as plt
import os
import base64

app = Flask(__name__)
data = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
    global data
    file = request.files['file']
    file_ext = file.filename[-4:]
    columns_selected = []
    display_column,unique_count,unique_values = [],[],[]
    if file_ext == '.csv':
        data = pd.read_csv(file,sep='\t')
    elif file_ext == 'xlsx':
        data = pd.read_xlsx(file)
    else:
        return "Please upload either csv file or excel file!"
    
    for col in data.columns:
        if data[col].dtype != object:
            display_column.append(col)
            unique_count.append(data[col].nunique())
            unique_values.append(data[col].unique()[:5])

    return render_template("index.html",dis = display_column,uniq1= unique_count,uniq2 = unique_values)

@app.route('/results', methods=['POST'])
def results():
    global data
    res = []
    selected_rows = request.form.getlist('columns[]')
    for col in selected_rows:
        res.append(find_limits(data,col))
        if data[col].dtype != object:
            fig, ax = plt.subplots()
            ax.boxplot(data[col], vert=False)
            ax.set_title(col)
            
            filename = col + '_boxplot.png'
            filepath = os.path.join(app.static_folder, 'Images', filename)
            fig.savefig(filepath, dpi=150, bbox_inches='tight')
            plt.close(fig)
            
            filename = '/static/Images/' + filename
            
    return render_template("results.html",res = res,filename=filename)


if __name__ == '__main__':
    app.run(debug=True)
