
from flask import (Flask, flash, redirect, redirect, 
                    render_template, url_for, request, session)
from models.dbcursor import sql_cursor
from models.ormdb import db_schema, Reg

app = Flask(__name__, template_folder="static/html")

app.config.update(
TESTING = True,
SECRET_KEY ="123"
)


# +-------------------------+-------------------------+
# User Defined Lib 
# +-------------------------+-------------------------+

#from applib.lib import helpers as h 

# +-------------------------+-------------------------+

# +-------------------------+-------------------------+




@app.route("/")
def index():
        if "email" not in session:
            return redirect(url_for(".login"))
        with sql_cursor() as db:
            qry = db.query( Reg.id, Reg.email, Reg.fname, Reg.lname, Reg.referred, Reg.current_bal
            ).filter(
                Reg.email == session['email']
            ).first()
        
            return render_template("index.html", 
                            email=qry.email,
                            name = qry.lname,
                            id = qry.id,
                            bal= qry.current_bal,
                            ref = qry.referred,
                            )
        return render_template("index.html")


#contact function
@app.route("/contact")
def contact():
    return render_template("contact.html")


# login function
@app.route("/login", methods = ["POST", "GET"])
def login():
    session["logged_in"] = None
    error = "USERNAME OR PASSWORD NOT CORRECT"
    if request.method == "POST":
        form = request.form
        _email = form.get("email")
        _password = form.get("password")
        with sql_cursor() as db:
            qry = db.query( Reg.id, Reg.email, Reg.fname, Reg.lname, Reg.referred, Reg.password, Reg.current_bal).filter(
                Reg.email == _email
            ).first()
        try:
            if (qry.password) == _password:
                session["myid"] = qry.id
                session["email"] = qry.email
                session["logged_in"] = True
               
                return render_template("user_profile.html",
                        email = qry.email, 
                        name = qry.fname, 
                        bal= qry.current_bal,
                        ref = qry.referred,
                        id = qry.id
                        )
            else:
                error = error
            
                return redirect(url_for(".login", error=error ) )
        except:
            error = "Login Unsuccessful"
            return redirect(url_for("login.html", error = error) )       
        
    return render_template("login.html")

# Registration  function   
@app.route("/reg", methods=["POST", "GET"])
def reg():
    if request.method == "POST":
        form = request.form
        fname = form.get("fname")
        lname = form.get("lname")
        gender = form.get("gender")
        email = form.get("email")
        password = form.get("password")
        with sql_cursor() as db:
            reg = Reg()
            reg.fname = fname
            reg.lname = lname
            reg.email = email
            reg.gender = gender
            reg.password = password
            db.add(reg)
            return redirect(url_for(".login"))
    return render_template("reg.html")



@app.route("/dashboard", methods=["POST","GET"])
def user_profile():
    if "email" not in session:
        return redirect(url_for(".login"))
    with sql_cursor() as db:
        qry = db.query( Reg.id, Reg.email, Reg.fname, Reg.lname, Reg.referred, Reg.current_bal
        ).filter(
            Reg.email == session['email']
        ).first()
       
        return render_template("user_profile.html", 
                         email=qry.email,
                         name = qry.lname,
                         id = qry.id,
                         bal= qry.current_bal,
                         ref = qry.referred,
                          )
 
        


@app.route("/setting", methods=["POST", "GET"])
def setting():
     # 1 usd per referera
    form =  request.form
    amount = 100.00
    number_of_user_refered = 1
    if request.method == "POST":
        ref = form.get("ref", 0)
        with sql_cursor() as db:
            qry = db.query( Reg.email, Reg.fname, Reg.lname, 
                            Reg.referred, 
                            Reg.current_bal , Reg.id
                          ).filter(
                                    Reg.id == ref
                                   ).first()
            
            if qry: # (qry.id == ref):
                # if qry:
               # import pdb;pdb.set_trace()
                temp_current_bal = qry.current_bal or 0
                temp_referred = qry.referred  or 0
                balance = int(temp_current_bal)  + int(amount)
                _referred = int(temp_referred ) + int(number_of_user_refered)
                db.query(Reg).filter(
                                        Reg.id == qry.id
                                    ).update({        
                                              "current_bal" : balance,
                                                "referred" : _referred
                                            })
                return render_template("user_profile.html")
    return render_template("setting.html")

@app.route("/logout")
def logout():
    session.pop("email" , None)
    return render_template("login.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6060, debug=True)