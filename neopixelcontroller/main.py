from __future__ import print_function
from flask import Flask, render_template, url_for, request, redirect, jsonify, abort
from flask_wtf import CSRFProtect, FlaskForm
from lib.color import Color
from lib.controller import Controller
from tinydb import TinyDB, Query
import atexit
import os


def main():
    app = Flask(__name__)
    controller = Controller()
    db = TinyDB('data/database.json')
    query = Query()

    app.config['SECRET_KEY'] = os.urandom(24)

    CSRFProtect(app)

    main.color = Color(0, 0, 0)
    main.brightness = 255
    main.state = False
    main.effects = []

    @app.before_first_request
    def init():
        if db.search(query.color != ''):
            result = db.get(query.color != '')['color'].split(',')
            main.color = Color(int(result[0]), int(result[1]), int(result[2]))

        if db.search(query.brightness != ''):
            result = db.get(query.brightness != '')
            main.brightness = result['brightness']

        if db.search(query.state != ''):
            result = db.get(query.state != '')
            main.state = bool(result['state'])

        if main.state:
            controller.color(main.color)
            controller.brightness(main.brightness)

        main.effects = controller.effects()

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            data = request.form

            main.color = Color(int(data['red']), int(data['green']), int(data['blue']))
            main.brightness = int(data['brightness'])

            controller.brightness(main.brightness)

            if data['submit'] == 'apply':
                main.state = True
                controller.clear()
                controller.color(main.color)
                controller.brightness(main.brightness)

            elif data['submit'] == 'effect':
                main.state = True
                controller.clear()
                controller.brightness(main.brightness)

                if data['effect'] in main.effects:
                    controller.start_effect(data['effect'], Color(int(data['red']), int(data['green']), int(data['blue'])))
            elif data['submit'] == 'off':
                main.state = False
                controller.clear()

            if main.state:
                db.update({'color': main.color.__str__()}, query.color != '')
                db.update({'brightness': main.brightness}, query.brightness != '')

            db.update({'state': main.state}, query.state != '')

            return redirect(url_for('index'))

        return render_template('index.html', effects=main.effects, color=main.color, brightness=main.brightness)

    @app.route('/api/v1.0/state/<string:state>', methods=['GET'])
    def state(state):
        if not state:
            abort(400)

        main.state = True if state == 'true' else False
        db.update({'state': main.state}, query.state != '')
        controller.clear()

        if main.state:
            controller.color(main.color)
            controller.brightness(main.brightness)

        return jsonify({'state': main.state}), 201

    @app.route('/api/v1.0/color/<int:red>/<int:green>/<int:blue>', methods=['GET'])
    def color(red, green, blue):
        if not red or not green or not blue:
            abort(400)

        main.state = True
        main.color = Color(int(red), int(green), int(blue))
        controller.color(main.color)
        db.update({'color': main.color.__str__()}, query.color != '')

        return jsonify({'color': main.color.__str__()}), 201

    @app.route('/api/v1.0/brightness/<int:brightness>', methods=['GET'])
    def brightness(brightness):
        if not brightness:
            abort(400)

        main.state = True
        main.brightness = int(brightness)
        controller.brightness(main.brightness)
        db.update({'brightness': main.brightness}, query.brightness != '')

        return jsonify({'brightness': main.brightness}), 201

    app.run(host='0.0.0.0', port=5000)
    db.close()
    atexit.register(controller.__exit__)

if __name__ == '__main__':
    main()
