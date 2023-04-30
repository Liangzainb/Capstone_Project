from flask import Flask, Blueprint, render_template, redirect, url_for, request
from werkzeug.middleware.proxy_fix import ProxyFix
import sys
from argparse import ArgumentParser
from cvd_model import *

appweb = Blueprint('hello', __name__)


@appweb.route('/')
def home():
    return render_template("index.html")


@appweb.route('/send', methods=['POST'])
def send(predict=predict):
    if request.method == 'POST':
        patient_age = request.form['age']       # 1
        patient_gender = request.form['gender']       # 2
        patient_polyuria = request.form['polyuria']       # 3
        patient_polydipsia = request.form['polydipsia']       # 4
        patient_sudden_weight_loss = request.form['suddenweightloss']       # 5
        patient_weakness = request.form['weakness']       # 6
        patient_polyphagia = request.form['polyphagia']       # 7
        patient_genital_thrush = request.form['genitalthrush']       # 8
        patient_visual_blurring = request.form['visualblurring']       # 9
        patient_itching = request.form['itching']       # 10
        patient_irritability = request.form['irritability']       # 11
        patient_delayed_healing = request.form['delayedhealing']       # 12
        patient_partial_paresis = request.form['partialparesis']       # 13
        patient_muscle_stiffness = request.form['musclestiffness']       # 14
        patient_alopecia = request.form['alopecia']       # 15
        patient_obesity = request.form['obesity']       # 16

        if patient_gender == "male":
            patient_gender = 1
        else:
            patient_gender = 0

        if patient_polyuria == "Yes":
            patient_polyuria = 1
        else:
            patient_polyuria = 0

        if patient_polydipsia == "Yes":
            patient_polydipsia = 1
        else:
            patient_polydipsia = 0

        if patient_sudden_weight_loss == "Yes":
            patient_sudden_weight_loss = 1
        else:
            patient_sudden_weight_loss = 0

        if patient_weakness == "Yes":
            patient_weakness = 1
        else:
            patient_weakness = 0

        if patient_polyphagia == "Yes":
            patient_polyphagia = 1
        else:
            patient_polyphagia = 0

        if patient_genital_thrush == "Yes":
            patient_genital_thrush = 1
        else:
            patient_genital_thrush = 0

        if patient_visual_blurring == "Yes":
            patient_visual_blurring = 1
        else:
            patient_visual_blurring = 0

        if patient_itching == "Yes":
            patient_itching = 1
        else:
            patient_itching = 0

        if patient_irritability == "Yes":
            patient_irritability = 1
        else:
            patient_irritability = 0

        if patient_delayed_healing == "Yes":
            patient_delayed_healing = 1
        else:
            patient_delayed_healing = 0

        if patient_partial_paresis == "Yes":
            patient_partial_paresis = 1
        else:
            patient_partial_paresis = 0

        if patient_muscle_stiffness == "Yes":
            patient_muscle_stiffness = 1
        else:
            patient_muscle_stiffness = 0

        if patient_alopecia == "Yes":
            patient_alopecia = 1
        else:
            patient_alopecia = 0

        if patient_obesity == "Yes":
            patient_obesity = 1
        else:
            patient_obesity = 0

        # Accuracy of Model
        model.fit(x_train, y_train)    # <-- this line
        acc = model.score(x_train, y_train)

        predict_real = model.predict([[patient_age, patient_gender, patient_polyuria, patient_polydipsia,
                                       patient_sudden_weight_loss, patient_weakness, patient_polyphagia,
                                       patient_genital_thrush, patient_visual_blurring, patient_itching,
                                       patient_irritability, patient_delayed_healing, patient_partial_paresis,
                                       patient_muscle_stiffness, patient_alopecia, patient_obesity]])

        if predict_real == [0]:
            predict = "The result returned with " + str(round(acc, 2)*100) + "% accuracy and you have a lower " \
                                                                             "chance of getting diabetes"
        else:
            predict = "The result returned with " + str(round(acc, 2)*100) + "% accuracy and you have a higher " \
                                                                             "chance of getting diabetes"

        return render_template('index.html', predict=predict)

    else:
        return render_template('index.html', predict=predict)


@appweb.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':

    # arg parser for the standard anaconda-project options
    parser = ArgumentParser(prog="home",
                            description="Simple Flask Application")
    parser.add_argument('--anaconda-project-host', action='append', default=[],
                        help='Hostname to allow in requests')
    parser.add_argument('--anaconda-project-port', action='store', default=8086, type=int,
                        help='Port to listen on')
    parser.add_argument('--anaconda-project-iframe-hosts',
                        action='append',
                        help='Space-separated hosts which can embed us in an iframe per our Content-Security-Policy')
    parser.add_argument('--anaconda-project-no-browser', action='store_true',
                        default=False,
                        help='Disable opening in a browser')
    parser.add_argument('--anaconda-project-use-xheaders',
                        action='store_true',
                        default=False,
                        help='Trust X-headers from reverse proxy')
    parser.add_argument('--anaconda-project-url-prefix', action='store', default='',
                        help='Prefix in front of urls')
    parser.add_argument('--anaconda-project-address',
                        action='store',
                        # default='0.0.0.0',
                        help='IP address the application should listen on.')

    args = parser.parse_args()

    app = Flask(__name__)
    app.register_blueprint(appweb, url_prefix=args.anaconda_project_url_prefix)

    app.config['PREFERRED_URL_SCHEME'] = 'https'

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host=args.anaconda_project_address, port=args.anaconda_project_port)
