from flask import Flask,render_template,request
from application.models.database import db_session
from application.models.models import UsageHistory
import datetime

app = Flask(__name__)

def calc():
    all_history = UsageHistory.query.all()
    sum = 0
    for history in all_history:
        sum += history.value
    return sum

# def make_image():
#     all_history = UsageHistory.query.all()
#     time = []
#     val = []
#     fig = plt.figure()
#     current_sum = 0
#     current_time = 0
#     for history in all_history:
#         current_sum += history.value
#         current_time += 1
#         time.append(current_time)
#         val.append(current_sum)
#     plt.plot(time, val)
#     fig.savefig('./application/static/images/graph.png')

@app.route("/")
def hello():
    #make_image()
    return index()


@app.route("/index")
def index():
    sum = calc()
    #make_image()
    all_history = UsageHistory.query.all()
    return render_template("index.html",all_history=all_history,sum=sum,invalid=False)

@app.route("/index")
def input_error():
    sum = calc()
    all_history = UsageHistory.query.all()
    return render_template("index.html",all_history=all_history,sum=sum,invalid=True)

@app.route("/add",methods=["post"])
def add():
    title = request.form["title"]
    value = request.form["value"]
    if(str.isdecimal(value)):
        content = UsageHistory(title,value,datetime.date.today())
        db_session.add(content)
        db_session.commit()
        return index()
    else:
        return input_error()

@app.route("/delete",methods=["post"])
def delete():
    id_list = request.form.getlist("delete")
    for id in id_list:
        content = UsageHistory.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    return index()

if __name__ == "__main__":
    app.run(debug=True)