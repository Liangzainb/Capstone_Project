import tkinter as tk
from cvd_model import *


class CVD_GUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tk.Tk()
        self.main_window.title("Diabetes"
                               " Predictor")

        # Create two frames to group widgets.
        self.zero_frame = tk.Frame()
        self.one_frame = tk.Frame()
        self.two_frame = tk.Frame()
        self.three_frame = tk.Frame()
        self.four_frame = tk.Frame()
        self.five_frame = tk.Frame()
        self.six_frame = tk.Frame()
        self.seven_frame = tk.Frame()
        self.eight_frame = tk.Frame()
        self.nine_frame = tk.Frame()
        self.ten_frame = tk.Frame()
        self.eleven_frame = tk.Frame()
        self.twelve_frame = tk.Frame()
        self.thirteen_frame = tk.Frame()
        self.fourteen_frame = tk.Frame()
        self.fifteen_frame = tk.Frame()
        self.sixteen_frame = tk.Frame()
        self.seventeen_frame = tk.Frame()

        # Create the widgets for zero frame. (0 title display)
        self.title_label = tk.Label(self.zero_frame, text='DIABETES PREDICTOR', fg="Red", font=("Helvetica", 18))
        self.title_label.pack()

        # Create the widgets for one frame. (1 age input)
        self.age_label = tk.Label(self.one_frame, text='1.Age:')
        self.age_entry = tk.Entry(self.one_frame, bg="white", fg="black", width=10)
        # self.age_entry.insert(0,'50')
        self.age_label.pack(side='left')
        self.age_entry.pack(side='left')

        # Create the widgets for two frame. (2 gender input)
        self.gender_label = tk.Label(self.two_frame, text='2.gender:')
        self.click_gender_var = tk.StringVar()
        self.click_gender_var.set("Male")
        self.gender_inp = tk.OptionMenu(self.two_frame, self.click_gender_var, "Male", "Female")
        self.gender_label.pack(side='left')
        self.gender_inp.pack(side='left')

        # Create the widgets for three frame. (3 polyuria symptom input)
        self.polyuria_label = tk.Label(self.three_frame, text='3.Do you have the symptom of polyuria?')
        self.click_polyuria_var = tk.StringVar()
        self.click_polyuria_var.set("No")
        self.polyuria_inp = tk.OptionMenu(self.three_frame, self.click_polyuria_var, "No", "Yes")
        self.polyuria_label.pack(side='left')
        self.polyuria_inp.pack(side='left')

        # Create the widgets for four frame. (4 polydipsia symptom input)
        self.polydipsia_label = tk.Label(self.four_frame, text='4.Do you have the symptom of polydipsia?')
        self.click_polydipsia_var = tk.StringVar()
        self.click_polydipsia_var.set("No")
        self.polydipsia_inp = tk.OptionMenu(self.four_frame, self.click_polydipsia_var, "No", "Yes")
        self.polydipsia_label.pack(side='left')
        self.polydipsia_inp.pack(side='left')

        # Create the widgets for five frame. (5 sudden_weight_loss symptom input)
        self.sudden_weight_loss_label = tk.Label(self.five_frame, text='5.Do you have the symptom of '
                                                                       'sudden weight loss?')
        self.click_sudden_weight_loss_var = tk.StringVar()
        self.click_sudden_weight_loss_var.set("No")
        self.sudden_weight_loss_inp = tk.OptionMenu(self.five_frame, self.click_sudden_weight_loss_var, "No", "Yes")
        self.sudden_weight_loss_label.pack(side='left')
        self.sudden_weight_loss_inp.pack(side='left')

        # Create the widgets for six frame. (6 weakness symptom input)
        self.weakness_label = tk.Label(self.six_frame, text='6.Do you have the symptom of weakness?')
        self.click_weakness_var = tk.StringVar()
        self.click_weakness_var.set("No")
        self.weakness_inp = tk.OptionMenu(self.six_frame, self.click_weakness_var, "No", "Yes")
        self.weakness_label.pack(side='left')
        self.weakness_inp.pack(side='left')

        # Create the widgets for seven frame. (7 polyphagia symptom input)
        self.polyphagia_label = tk.Label(self.seven_frame, text='7.Do you have the symptom of polyphagia?')
        self.click_polyphagia_var = tk.StringVar()
        self.click_polyphagia_var.set("No")
        self.polyphagia_inp = tk.OptionMenu(self.seven_frame, self.click_polyphagia_var, "No", "Yes")
        self.polyphagia_label.pack(side='left')
        self.polyphagia_inp.pack(side='left')

        # Create the widgets for eight frame. (8 genital_thrush symptom input)
        self.genital_thrush_label = tk.Label(self.eight_frame, text='8.Do you have the symptom of genital thrush?')
        self.click_genital_thrush_var = tk.StringVar()
        self.click_genital_thrush_var.set("No")
        self.genital_thrush_inp = tk.OptionMenu(self.eight_frame, self.click_genital_thrush_var, "No", "Yes")
        self.genital_thrush_label.pack(side='left')
        self.genital_thrush_inp.pack(side='left')

        # Create the widgets for nine frame. (9 symptom visual_blurring input)
        self.visual_blurring_label = tk.Label(self.nine_frame, text='9.Do you have the symptom of visual_blurring?')
        self.click_visual_blurring_var = tk.StringVar()
        self.click_visual_blurring_var.set("No")
        self.visual_blurring_inp = tk.OptionMenu(self.nine_frame, self.click_visual_blurring_var, "No", "Yes")
        self.visual_blurring_label.pack(side='left')
        self.visual_blurring_inp.pack(side='left')

        # Create the widgets for ten frame. (10 itching symptom input)
        self.itching_label = tk.Label(self.ten_frame, text='10.Do you have the symptom of itching?')
        self.click_itching_var = tk.StringVar()
        self.click_itching_var.set("No")
        self.itching_inp = tk.OptionMenu(self.ten_frame, self.click_itching_var, "No", "Yes")
        self.itching_label.pack(side='left')
        self.itching_inp.pack(side='left')

        # Create the widgets for eleven frame. (11 irritability symptom input)
        self.irritability_label = tk.Label(self.eleven_frame, text='11.Do you have the symptom of irritability?')
        self.click_irritability_var = tk.StringVar()
        self.click_irritability_var.set("No")
        self.irritability_inp = tk.OptionMenu(self.eleven_frame, self.click_irritability_var, "No", "Yes")
        self.irritability_label.pack(side='left')
        self.irritability_inp.pack(side='left')

        # Create the widgets for twelve frame. (12 delayed_healing symptom input)
        self.delayed_healing_label = tk.Label(self.twelve_frame, text='12.Do you have the symptom of delayed_healing?')
        self.click_delayed_healing_var = tk.StringVar()
        self.click_delayed_healing_var.set("No")
        self.delayed_healing_inp = tk.OptionMenu(self.twelve_frame, self.click_delayed_healing_var, "No", "Yes")
        self.delayed_healing_label.pack(side='left')
        self.delayed_healing_inp.pack(side='left')

        # Create the widgets for thirteen frame. (13 partial_paresis symptom input)
        self.partial_paresis_label = tk.Label(self.thirteen_frame, text='13.Do you have the symptom of partial_paresis?')
        self.click_partial_paresis_var = tk.StringVar()
        self.click_partial_paresis_var.set("No")
        self.partial_paresis_inp = tk.OptionMenu(self.thirteen_frame, self.click_partial_paresis_var, "No", "Yes")
        self.partial_paresis_label.pack(side='left')
        self.partial_paresis_inp.pack(side='left')

        # Create the widgets for fourteen frame. (14 symptom input)
        self.muscle_stiffness_label = tk.Label(self.fourteen_frame, text='14.Do you have the symptom of '
                                                                         'muscle_stiffness?')
        self.click_muscle_stiffness_var = tk.StringVar()
        self.click_muscle_stiffness_var.set("No")
        self.muscle_stiffness_inp = tk.OptionMenu(self.fourteen_frame, self.click_muscle_stiffness_var, "No", "Yes")
        self.muscle_stiffness_label.pack(side='left')
        self.muscle_stiffness_inp.pack(side='left')

        # Create the widgets for fifteen frame. (15 symptom input)
        self.alopecia_label = tk.Label(self.fifteen_frame, text='15.Do you have the symptom of alopecia?')
        self.click_alopecia_var = tk.StringVar()
        self.click_alopecia_var.set("No")
        self.alopecia_inp = tk.OptionMenu(self.fifteen_frame, self.click_alopecia_var, "No", "Yes")
        self.alopecia_label.pack(side='left')
        self.alopecia_inp.pack(side='left')

        # Create the widgets for sixteen frame. (16 symptom input)
        self.obesity_label = tk.Label(self.sixteen_frame, text='16.Do you have the symptom of obesity?')
        self.click_obesity_var = tk.StringVar()
        self.click_obesity_var.set("No")
        self.obesity_inp = tk.OptionMenu(self.sixteen_frame, self.click_obesity_var, "No", "Yes")
        self.obesity_label.pack(side='left')
        self.obesity_inp.pack(side='left')

        # Create the widgets for fifteen frame = diabetes (17 prediction of heart disease)
        self.diabetes_predict_ta = tk.Text(self.seventeen_frame, height=10, width=25, bg='light blue')

        # Create predict button and quit button
        self.btn_predict = tk.Button(self.seventeen_frame, text='Predict Diabetes', command=self.predict_diabetes)
        self.btn_quit = tk.Button(self.seventeen_frame, text='Quit', command=self.main_window.destroy)

        self.diabetes_predict_ta.pack(side='left')
        self.btn_predict.pack()
        self.btn_quit.pack()

        # Pack the frames.
        self.zero_frame.pack()
        self.one_frame.pack()
        self.two_frame.pack()
        self.three_frame.pack()
        self.four_frame.pack()
        self.five_frame.pack()
        self.six_frame.pack()
        self.seven_frame.pack()
        self.eight_frame.pack()
        self.nine_frame.pack()
        self.ten_frame.pack()
        self.eleven_frame.pack()
        self.twelve_frame.pack()
        self.thirteen_frame.pack()
        self.fourteen_frame.pack()
        self.fifteen_frame.pack()
        self.sixteen_frame.pack()
        self.seventeen_frame.pack()

        # Enter the tkinter main loop.
        tk.mainloop()

    def predict_diabetes(self):
        result_string = ""

        self.diabetes_predict_ta.delete(0.0, tk.END)
        patient_age = self.age_entry.get()        # 1

        patient_gender = self.click_gender_var.get()        # 2
        if patient_gender == "Male":
            patient_gender = 1
        else:
            patient_gender = 0

        patient_polyuria = self.click_polyuria_var.get()        # 3
        if patient_polyuria == "Yes":
            patient_polyuria = 1
        else:
            patient_polyuria = 0

        patient_polydipsia = self.click_polydipsia_var.get()        # 4
        if patient_polydipsia == "Yes":
            patient_polydipsia = 1
        else:
            patient_polydipsia = 0

        patient_sudden_weight_loss = self.click_sudden_weight_loss_var.get()        # 5
        if patient_sudden_weight_loss == "Yes":
            patient_sudden_weight_loss = 1
        else:
            patient_sudden_weight_loss = 0

        patient_weakness = self.click_weakness_var.get()        # 6
        if patient_weakness == "Yes":
            patient_weakness = 1
        else:
            patient_weakness = 0

        patient_polyphagia = self.click_polyphagia_var.get()        # 7
        if patient_polyphagia == "Yes":
            patient_polyphagia = 1
        else:
            patient_polyphagia = 0

        patient_genital_thrush = self.click_genital_thrush_var.get()        # 8
        if patient_genital_thrush == "Yes":
            patient_genital_thrush = 1
        else:
            patient_genital_thrush = 0

        patient_visual_blurring = self.click_visual_blurring_var.get()        # 9
        if patient_visual_blurring == "Yes":
            patient_visual_blurring = 1
        else:
            patient_visual_blurring = 0

        patient_itching = self.click_itching_var.get()        # 10
        if patient_itching == "Yes":
            patient_itching = 1
        else:
            patient_itching = 0

        patient_irritability = self.click_irritability_var.get()            # 11
        if patient_irritability == "Yes":
            patient_irritability = 1
        else:
            patient_irritability = 0

        patient_delayed_healing = self.click_delayed_healing_var.get()        # 12
        if patient_delayed_healing == "Yes":
            patient_delayed_healing = 1
        else:
            patient_delayed_healing = 0

        patient_partial_paresis = self.click_partial_paresis_var.get()        # 13
        if patient_partial_paresis == "Yes":
            patient_partial_paresis = 1
        else:
            patient_partial_paresis = 0

        patient_muscle_stiffness = self.click_muscle_stiffness_var.get()        # 14
        if patient_muscle_stiffness == "Yes":
            patient_muscle_stiffness = 1
        else:
            patient_muscle_stiffness = 0

        patient_alopecia = self.click_alopecia_var.get()        # 15
        if patient_alopecia == "Yes":
            patient_alopecia = 1
        else:
            patient_alopecia = 0

        patient_obesity = self.click_obesity_var.get()        # 16
        if patient_obesity == "Yes":
            patient_obesity = 1
        else:
            patient_obesity = 0

        result_string += "===Patient Diagnosis=== \n"
        patient_info = (patient_age, patient_gender, patient_polyuria, patient_polydipsia, patient_sudden_weight_loss,
                        patient_weakness, patient_polyphagia, patient_genital_thrush, patient_visual_blurring,
                        patient_itching, patient_irritability, patient_delayed_healing, patient_partial_paresis,
                        patient_muscle_stiffness, patient_alopecia, patient_obesity)

        diabetes_prediction = best_model.predict([patient_info])
        disp_string = ("This prediction has an accuracy of:", str(model_accuracy))

        result = diabetes_prediction

        if diabetes_prediction == [0]:
            result_string = (disp_string, '\n', "0 - You have lower risk of diabetes")
        else:
            result_string = (disp_string, '\n'+"1 - You have higher risk of diabetes, please consult your GP soon")
        self.diabetes_predict_ta.insert('1.0', result_string)
        # Predicted:  1 Actual:  1 Data:  (11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        # Predicted:  0 Actual:  0 Data:  (2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        # Predicted:  0 Actual:  1 Data:  (21, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0)

my_cvd_GUI = CVD_GUI()
