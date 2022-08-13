from flask import *
import translate

app = Flask(__name__)


@app.route('/')
def get_translation():
    text = request.args.get('text')
    language = request.args.get('lang')
    translate1 = translate.Translate(text, language)
    data = {"Translation": translate1.get_translate()}
    json_dump = json.dumps(data)
    return json_dump


if __name__ == '__main__':
    app.run(port=7777)