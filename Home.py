from flask import*
import sqlite3

app=Flask(__name__)
app.secret_key = "message"

@app.route("/login",methods=['POST','GET'])
def login():
    con = sqlite3.connect('datatwo.db')
    cur = con.cursor()
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cur.execute("SELECT * FROM user WHERE Username = ? and Password = ?", (username, password,))
        account = cur.fetchone()
        print("new")
        if account:
            flash("Successfully logged in")
            return redirect(url_for('login'))
        else:
            flash('Incorrect username / password !')
    return render_template("login.html")

@app.route("/registration",methods=['POST','GET'])
def registration():
    if request.method=='POST':
        try:
            name = request.form["name"]
            lname = request.form["lname"]
            date=request.form["birthday"]
            username = request.form["username"]
            password = request.form["password"]
            con = sqlite3.connect('datatwo.db')
            cur = con.cursor()
            cur.execute('SELECT * FROM user WHERE Username = ?', (username,))
            account = cur.fetchone()
            print("yes")
            if account:
                flash('Username already exists !')
                return redirect(url_for("registration"))
            else:
                cur.execute("insert into user(Name,Last_Name,DOB,Username,Password) values(?,?,?,?,?)", (name, lname, date, username, password))
                con.commit()
                flash("You have Registered successfully", "info")
                return redirect(url_for("login"))
        except:
            print("Error")
            flash("We can not regiter with your data")
    return render_template("register.html")

if __name__=="__main__":
    app.run(debug=True)