<form action="/userid" method="POST">
    <div class="container">
        <div class="row">
            <div class="col">
                <label> referral Id </label>
                <input type="text" name="ref_id" value="{{ref_id}}"> 
             <button type="submit" > Save </button>
            </div>
        </div>
    </div>
</form>



 addEventListener("load", function () {
      	setTimeout(hideURLbar, 0);
      }, false);
      
      function hideURLbar() {
      	window.scrollTo(1, 1);
      }



      <section class="w3l-banner">
			<div class="nav-sec  position-relative">
			<nav>
					<ul id="menu">
				  <li>
					<input id="check01" type="checkbox" name="menu"/>
					<label class="menulist" for="check01">&nbsp;</label>
					<ul class="submenu">
						{% if  session.logged_in %}
						<li> <a href="{{url_for('.user_profile')}}"> Dasboard</a></li>
						<li><a href="{{url_for('.index')}}" class="acive">Home</a></li>
						<li><a href="#about" class="scroll">About</a></li>
						<li><a href="#service" class="scroll">Services</a></li>
						<li><a href="#news" class="scroll">News</a></li>
						<li><a href="{{url_for('.contact')}}"> Contact </a></li>
						<li><a href="{{url_for('.logout')}}"> Logout </a></li>

                        
						{% else %}
						<li><a href="{{url_for('.index')}}" class="acive">Home</a></li>
						<li><a href="#about" class="scroll">About</a></li>
						<li><a href="#service" class="scroll">Services</a></li>
						<li><a href="#news" class="scroll">News</a></li>
						<li><a href="{{url_for('.login')}}"> Login </a></li>
						<li><a href="{{url_for('.contact')}}"> Contact </a></li>
						
						{% endif %}
					</ul>
				  </li>
				</ul>
				</nav>
			</div>
	</section>





	
    # 1 usd per referera
    form =  request.form
    amount = 1
    number_of_user_refered = 1
    # ref = request.args.get("ref")
    if request.method == "POST":
        ref = form.get("ref")
        with sql_cursor() as db:
            qry = db.query(Reg.id, Reg.current_bal, Reg.referred ).filter(
                Reg.id == ref)
            if (qry.id == ref):
                #trying to console the output
                print(qry)
                #tryiny to manipulate the  the outputed data
                balance = int(qry.current_bal  + amount)
                _referred = int(qry.referred + number_of_user_refered)
                #nested query inorder to update the manipulated data
                with sql_cursor() as db:
                    db.query(Reg.id, Reg.current_bal, Reg.referred).filter(
                        Reg.id == ref
                        #update d db
                    ).update({        
                "current_bal" : balance,
                "referred" : _referred

                })
@app.route("/userid", methods=["POST","GET"])
def user_profile():
    if "email" not in session:
        return redirect(url_for(".login"))
    with sql_cursor() as db:
        user = db.query(Reg.email, Reg.fname, Reg.lname, Reg.current_bal
        ).filter(
            Reg.email == session['email']
        ).first()
        return render_template("user_profile.html", email = qry.email, name = qry.fname)
        



##################################################
# the corrected setting
##################################################
def setting():
     # 1 usd per referera
    form =  request.form
    amount = 1
    number_of_user_refered = 1    if request.method == "POST":
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
                import pdb;pdb.set_trace()

                temp_current_bal = qry.current_bal or 0 
                temp_referred = qry.referred or 0 
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
    
