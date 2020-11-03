from flask import Flask,jsonify,request,render_template
from Wikipens import wikipen,contenttor,suggestions

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/content/')
def contents():
    query=request.args.get('q')
    tittle,url,cont,status=contenttor(query)
    suggested=suggestions(query,5)
    a={"page found":status,"search":query,"tittle":tittle,"url":url}
    b={"content":cont}
    c={"other suggestions":suggested}
    return jsonify({"page":b,"details":a,"suggestions":c})



@app.route('/page/')
def page():
    query=request.args.get('q')
    tittle,url,summary,images,status=wikipen(query)
    suggested=suggestions(query,5)
    a={"page found":status,"search":query,"tittle":tittle,"url":url}
    b={"summary":summary,"images":images}
    c={"other suggestions":suggested}
    return jsonify({"page":b,"details":a,"suggestions":c})

@app.route('/search/')
def onlysearch():
    query=request.args.get('q')
    suggested=suggestions(query,100)
    c={"search related suggestions":suggested}
    return jsonify(c)


if __name__ == "__main__":
    app.debug = True
    app.run()
