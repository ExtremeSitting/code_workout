#! /usr/bin/env python

from flask import Flask, jsonify, make_response, request, abort
app = Flask(__name__)


things = []


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def find_thing(thing_id):
    thing = [thing for thing in things if thing['id'] == thing_id]
    if not thing:
        abort(404)
    else:
        return thing[0]


@app.route('/things', methods=['GET'])
def return_things():
    if not things:
        return jsonify({'things': 'No things'})
    else:
        return jsonify({'things': things})


@app.route('/things/<int:thing_id>', methods=['GET'])
def get_thing(thing_id):
    thing = find_thing(thing_id)
    return jsonify({'thing': thing})


@app.route('/things', methods=['POST'])
def create_thing():
    if not request.json or 'name' not in request.json:
        abort(400)
    try:
        new_id = things[-1]['id'] + 1
    except IndexError:
        new_id = 1
    thing = {
        'id': new_id,
        'name': request.json['name'],
        'value': request.json.get('value', None),
        'device': request.json.get('device', None)
    }
    things.append(thing)
    return jsonify({'thing': thing}), 201


@app.route('/things/<int:thing_id>', methods=['DELETE'])
def remove_thing(thing_id):
    things.remove(find_thing(thing_id))
    return jsonify({'DELETE': thing_id}), 201


if __name__ == '__main__':
    app.run(debug=True)
