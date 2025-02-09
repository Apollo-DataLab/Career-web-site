from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [

    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Athens, Greece',
        'salary': '€20,000''
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Athens, Greece',
        'salary': '€30,000'    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': '€15,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Remote',
        'salary': '€25,000'
    
    }
]

@app.route('/')
def index():
    return render_template('home.html', jobs=jobs) 

@app.route('/api/jobs')
def list_jobs():
    return jsonify(jobs)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
