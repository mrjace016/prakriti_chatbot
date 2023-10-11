from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ayurvedic Prakriti assessment logic
def assess_prakriti(answers):
    vata_score = sum(answers[:5])
    pitta_score = sum(answers[5:10])
    kapha_score = sum(answers[10:])
    prakriti = ""

    if vata_score > pitta_score and vata_score > kapha_score:
        prakriti = "Vata"
    elif pitta_score > vata_score and pitta_score > kapha_score:
        prakriti = "Pitta"
    else:
        prakriti = "Kapha"

    return prakriti

# Questions and explanations
questions = [
    ("q1", "Do you often feel cold?", "1 (Not at all)", "5 (Very often)"),
    ("q2", "Is your skin often dry?", "1 (Not at all)", "5 (Very often)"),
    ("q3", "Is your appetite irregular?", "1 (Not at all)", "5 (Very often)"),
    ("q4", "Do you tend to worry or feel anxious?", "1 (Not at all)", "5 (Very often)"),
    ("q5", "Are you often forgetful?", "1 (Not at all)", "5 (Very often)"),
    ("q6", "Is your skin prone to rashes or acne?", "1 (Not at all)", "5 (Very often)"),
    ("q7", "Do you have a strong appetite and get hungry easily?", "1 (Not at all)", "5 (Very often)"),
    ("q8", "Are you prone to anger or irritability?", "1 (Not at all)", "5 (Very often)"),
    ("q9", "Is your body temperature usually warm or hot?", "1 (Not at all)", "5 (Very often)"),
    ("q10", "Do you have a competitive nature?", "1 (Not at all)", "5 (Very often)"),
    ("q11", "Is your skin often oily?", "1 (Not at all)", "5 (Very often)"),
    ("q12", "Is your digestion slow and steady?", "1 (Not at all)", "5 (Very often)"),
    ("q13", "Do you have a calm and composed temperament?", "1 (Not at all)", "5 (Very often)"),
    ("q14", "Is your hair usually thick and oily?", "1 (Not at all)", "5 (Very often)"),
    ("q15", "Are you generally patient and forgiving?", "1 (Not at all)", "5 (Very often)"),
]

@app.route("/")
def introduction():
    return render_template("introduction.html")

@app.route("/index", methods=["GET", "POST"])
def index():
    prakriti = ""
    answers = []

    if request.method == "POST":
        for q, _, _, _ in questions:
            answer = int(request.form[q])
            answers.append(answer)
        prakriti = assess_prakriti(answers)

    return render_template("index.html", questions=questions, prakriti=prakriti)

if __name__ == "__main__":
    app.run(debug=True)
