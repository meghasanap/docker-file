

# app.py
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/data')
def get_data():
    file_name = request.args.get('n')
    line_number = request.args.get('m')

    if file_name:
        file_path = f'/tmp/data/{file_name}.txt'
        
        if line_number:
            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    return lines[int(line_number) - 1]
            except FileNotFoundError:
                return f"File {file_name}.txt not found."
            except IndexError:
                return f"Line {line_number} not found in {file_name}.txt."
        else:
            try:
                with open(file_path, 'r') as file:
                    return file.read()
            except FileNotFoundError:
                return f"File {file_name}.txt not found."

    return "Invalid request. Provide 'n' parameter."

if __name__ == '__main__':
    app.run(debug=True, port=8080)
