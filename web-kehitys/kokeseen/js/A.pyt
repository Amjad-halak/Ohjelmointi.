# ==========================================================================
# ملف app.py - ملخص Python Flask الشامل (Back-End)
# ==========================================================================
from flask import Flask, request, jsonify

app = Flask(__name__)

# 1. مسار GET يستقبل قيماً من الرابط (URL Parameters)
# للتجربة في المتصفح: http://127.0.0.1:5000/multiply/4/5
@app.route("/multiply/<int:a>/<int:b>")
def multiply(a, b):
    result = a * b
    # نُرجع النتيجة دائماً بصيغة JSON عبر jsonify
    return jsonify({
        "a": a,
        "b": b,
        "result": result
    })

# 2. مسار POST يستقبل بيانات JSON من الجافاسكريبت (fetch POST)
@app.route("/api/message", methods=["POST"])
def receive_message():
    data = request.get_json()          # قراءة الـ JSON القادم وتحويله لقاموس بايثون
    if not data or "name" not in data:
        return jsonify({"error": "Missing name"}), 400  # إرجاع كود خطأ 400

    user_name = data["name"]
    return jsonify({
        "status": "success",
        "reply": f"Hello {user_name}, data received!"
    }), 200

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=5000)