from flask import Flask, request, render_template
from random import choice

app = Flask(__name__)

questions = {
    "1": {
        "問題": "一次、二次および三次予防に関する記述である。最も適当なのはどれか。 1 つ選べ。",
        "選択肢": {
            1: "住民を対象とするがん検診は、一次予防である。",
            2: "ヒトパピローマウイルス（HPV）ワクチン接種は、二次予防である。",
            3: "脳卒中発症後の機能回復訓練は、二次予防である。",
            4: "職場におけるストレスチェックは、三次予防である。",
            5: "精神障害者に対する社会復帰支援は、三次予防である。"
        },
        "解答": "2",
        "解説": "解説はここです"
    }
    # 他の問題をここに追加
}

@app.route('/', methods=['GET', 'POST'])
def question():
    current_question = choice(list(questions.values()))  # ランダムに問題を選択
    if request.method == 'POST':
        user_answer = request.form.get('choice')
        correct_answer = current_question["解答"]
        explanation = current_question["解説"]
        if user_answer == correct_answer:
            result = "Correct"
        else:
            result = "Incorrect"
        return render_template('result.html', result=result, correct_answer=correct_answer, explanation=explanation)

    return render_template('index.html', question=current_question)

if __name__ == '__main__':
    app.run(debug=True)
