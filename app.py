from flask import Flask, jsonify, render_template

app = Flask(__name__)


JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Delhi, India',
        'salary':'10,00,000'
    },
    {
        'id':2,
        'title':'Scientist',
        'location':'Delhi, India',
        'salary':'15,00,000'
    },
    {
        'id':3,
        'title':'Frontend Engineer',
        'location':'Remote',
        'salary':'12,00,000'
    },
    {
        'id':4,
        'title':'Backend Engineer',
        'location':'Remote',        
    }
]

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

@app.route("/")
def hello_world():
    return render_template('index.html',jobs = JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)