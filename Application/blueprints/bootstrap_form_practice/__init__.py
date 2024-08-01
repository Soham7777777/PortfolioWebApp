from flask import Blueprint, render_template, request
from sqlalchemy.exc import IntegrityError
from .forms import StudentRegistrationForm
from Application import db
from .models import Student


bp = Blueprint('BootstrapFormPractice', __name__, url_prefix='/forms', static_folder='static', template_folder='templates')

@bp.route('/form1', methods=['GET', 'POST'])
def form1():
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        try:
            db.session.add(
                Student(
                    fname=form.fname.data,
                    mname=form.mname.data,
                    lname=form.lname.data,
                    course=form.course.data,
                    gender=form.gender.data,
                    phone=form.phone_no.data,
                    current_address=form.current_address.data,
                    email=form.email.data,
                    password=form.password.data
                )
            )
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return "You are already registered. Welcome Back!!"
        return "You've successfuly registered!!"

    return render_template('bootstrap_form_practice/form1.html', form=form)

@bp.route('/form2', methods=['GET', 'POST'])
def form2():
    return render_template('bootstrap_form_practice/form2.html')

@bp.route('/form3', methods=['GET', 'POST'])
def form3():
    return render_template('bootstrap_form_practice/form3.html')

@bp.route('/form4', methods=['GET', 'POST'])
def form4():
    return render_template('bootstrap_form_practice/form4.html')