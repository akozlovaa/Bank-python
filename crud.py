from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from model.BankService import BankService
import json

with open("C:/Users/A/PycharmProjects/Bank-python/secret.json", 'r') as f:
    SECRET = json.load(f)

SQLALCHEMY_TRACK_MODIFICATIONS = False
DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class VirtualBankService(BankService, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(32), unique=False)
    maintenance_fee_in_usd = db.Column(db.Integer, unique=False)
    plan_name = db.Column(db.String(32), unique=False)
    service_term = db.Column(db.String(32), unique=False)
    interest_rate_in_percents = db.Column(db.Float, unique=False)
    federal_funds_rate_in_percents = db.Column(db.Float, unique=False)
    discount_rate_in_percents = db.Column(db.Float, unique=False)
    service_type = db.Column(db.String(64), unique=False)
    account_balance_in_usd = db.Column(db.Float, unique=False)
    creator = db.Column(db.String(32), unique=False)
    memory_require = db.Column(db.Float, unique=False)

    def __init__(self, bank_name=None, maintenance_fee_in_usd=None, plan_name=None, service_term=None,
                 interest_rate_in_percents=None, federal_funds_rate_in_percents=None,
                 discount_rate_in_percents=None, service_type=None, account_balance_in_usd=None, creator=None,
                 memory_require=None):
        super().__init__(bank_name, maintenance_fee_in_usd, plan_name, service_term, interest_rate_in_percents,
                         federal_funds_rate_in_percents, discount_rate_in_percents, service_type,
                         account_balance_in_usd)
        self.creator = creator
        self.memory_require = memory_require


class VirtualBankServiceSchema(ma.Schema):
    class Meta:
        fields = ('bank_name', 'maintenance_fee_in_usd', 'plan_name', 'service_term',
                  'interest_rate_in_percents', 'federal_funds_rate_in_percents', 'discount_rate_in_percents',
                  'service_type', 'account_balance_in_usd', 'creator', 'memory_require')


virtual_bank_service_schema = VirtualBankServiceSchema()
virtual_bank_services_schema = VirtualBankServiceSchema(many=True)


@app.route("/virtual_bank_service", methods=["GET"])
def get_virtual_bank_service():
    all_virtual_bank_service = VirtualBankService.query.all()
    result = virtual_bank_services_schema.dump(all_virtual_bank_service)
    return jsonify({'virtual_bank_services': result})


@app.route("/virtual_bank_service/<id>", methods=["GET"])
def virtual_bank_service_detail(id):
    virtual_bank_service = VirtualBankService.query.get(id)
    if not virtual_bank_service:
        abort(404)
    return virtual_bank_service_schema.jsonify(virtual_bank_service)


@app.route("/virtual_bank_service", methods=["POST"])
def add_virtual_bank_service():
    virtual_bank_service = VirtualBankService(request.json['bank_name'],
                                              request.json['maintenance_fee_in_usd'],
                                              request.json['plan_name'],
                                              request.json['service_term'],
                                              request.json['interest_rate_in_percents'],
                                              request.json['federal_funds_rate_in_percents'],
                                              request.json['discount_rate_in_percents'],
                                              request.json['service_type'],
                                              request.json['account_balance_in_usd'],
                                              request.json['creator'],
                                              request.json['memory_require'])
    db.session.add(virtual_bank_service)
    db.session.commit()
    return virtual_bank_service_schema.jsonify(virtual_bank_service)


@app.route("/virtual_bank_service/<id>", methods=["PUT"])
def virtual_bank_service_update(id):
    virtual_bank_service = VirtualBankService.query.get(id)
    if not virtual_bank_service:
        abort(404)
    virtual_bank_service.bank_name = request.json['bank_name']
    virtual_bank_service.maintenance_fee_in_usd = request.json['maintenance_fee_in_usd']
    virtual_bank_service.plan_name = request.json['plan_name']
    virtual_bank_service.service_term = request.json['service_term']
    virtual_bank_service.interest_rate_in_percents = request.json['interest_rate_in_percents']
    virtual_bank_service.federal_funds_rate_in_percents = request.json['federal_funds_rate_in_percents']
    virtual_bank_service.discount_rate_in_percents = request.json['discount_rate_in_percents']
    virtual_bank_service.service_type = request.json['service_type']
    virtual_bank_service.account_balance_in_usd = request.json['account_balance_in_usd']
    virtual_bank_service.creator = request.json['creator']
    virtual_bank_service.memory_require = request.json['memory_require']
    db.session.commit()
    return virtual_bank_service_schema.jsonify(virtual_bank_service)


@app.route("/virtual_bank_service/<id>", methods=["DELETE"])
def virtual_bank_service_delete(id):
    virtual_bank_service = VirtualBankService.query.get(id)
    if not virtual_bank_service:
        abort(404)
    db.session.delete(virtual_bank_service)
    db.session.commit()
    return virtual_bank_service_schema.jsonify(virtual_bank_service)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='localhost')
