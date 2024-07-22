from flask import Flask, render_template_string

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gradio App</title>
    <style>
        html, body {
            height: 100%;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
        body {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        gradio-app {
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
</head>
<body>
    <script type="module" src="https://gradio.s3-us-west-2.amazonaws.com/4.37.2/gradio.js"></script>
    <gradio-app src="https://rafaldembski-d-logic.hf.space"></gradio-app>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')