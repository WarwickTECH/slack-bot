from flask import Flask, jsonify
from flask_restplus import Resource, Api, fields
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app,
          version='0.1',
          title='WarwickTECH API',
          description='This is the API resource for WarwickTECH'
)

slack = api.namespace('slack', description='Slash Commands for WarwickTECH Slack Bot')

@slack.route('/codeofconduct', methods=['POST'])
class CodeofConduct(Resource):
    def post(self):
        return jsonify(
            content_type='application/json',
            response_type='in_channel',
            text="bit.ly/WT-CodeOfConduct",
        )

@slack.route('/expensepolicy', methods=['POST'])
class ExpensePolicy(Resource):
    def post(self):
        return jsonify(
            content_type='application/json',
            response_type='in_channel',
            text="bit.ly/WT-ExpensePolicy",
        )

if __name__ == '__main__':
    app.run(debug=True)

