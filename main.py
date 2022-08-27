from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# A voice, was sounding far away...
# Never dying...
# In the distance heard,
# The wind calls her name.

# ♫ Thurisaz - Endless...
# https://open.spotify.com/track/6o00N22CZ9iy6XtCFSLOc1

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

class MemberModel(db.Model):
    memID = db.Column(db.Integer, primary_key=True)
    membernumber = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)

    address = db.Column(db.String(300), nullable=False)
    city = db.Column(db.String(100), nullable=False)

    status = db.Column(db.String(100), nullable=False)
    paymentstatus = db.Column(db.String(100), nullable=False)
    paymentamount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Member(membernumber={self.membernumber}, password={self.password}, fullname={self.fullname}, email={self.email}, phone={self.phone}, address={self.address}, city={self.city}, status={self.status},paymentstatus={self.paymentstatus}, paymentamount={self.paymentamount})"

member_put_args = reqparse.RequestParser()
member_put_args.add_argument('membernumber', type=int, required=True, help='Member number is required')
member_put_args.add_argument('password', type=str, required=True, help='Password is required')
member_put_args.add_argument('fullname', type=str, required=True, help='Full name is required')
member_put_args.add_argument('email', type=str, required=True, help='Email is required')
member_put_args.add_argument('phone', type=int, required=True, help='Phone is required')
member_put_args.add_argument('address', type=str, required=True, help='Address is required')
member_put_args.add_argument('city', type=str, required=True, help='City is required')
member_put_args.add_argument('status', type=str, required=True, help='Status is required')
member_put_args.add_argument('paymentstatus', type=str, required=True, help='Payment status is required')
member_put_args.add_argument('paymentamount', type=int, required=True, help='Payment amount is required')

member_update_args = reqparse.RequestParser()
member_update_args.add_argument('membernumber', type=int, required=True, help='Member number is required')
member_update_args.add_argument('password', type=str, required=True, help='Password is required')
member_update_args.add_argument('fullname', type=str, required=True, help='Full name is required')
member_update_args.add_argument('email', type=str, required=True, help='Email is required')
member_update_args.add_argument('phone', type=int, required=True, help='Phone is required')
member_update_args.add_argument('address', type=str, required=True, help='Address is required')
member_update_args.add_argument('city', type=str, required=True, help='City is required')
member_update_args.add_argument('status', type=str, required=True, help='Status is required')
member_update_args.add_argument('paymentstatus', type=str, required=True, help='Payment status is required')
member_update_args.add_argument('paymentamount', type=int, required=True, help='Payment amount is required')

resource_fields = {
    'memID': fields.Integer,
    'membernumber': fields.Integer,
    'password': fields.String,
    'fullname': fields.String,
    'email': fields.String,
    'phone': fields.Integer,
    'address': fields.String,
    'city': fields.String,
    'status': fields.String,
    'paymentstatus': fields.String,
    'paymentamount': fields.Integer
}

class Member(Resource):
    @marshal_with(resource_fields)
    def get(self, member_id):
        member = MemberModel.query.filter_by(memID=member_id).first()
        if member:
            return member
        else:
            abort(404, message="Member with Member ID: {} doesn't exist".format(member_id))
            # 404 is the code for Not Found

    @marshal_with(resource_fields)
    def put(self, member_id):
        args = member_put_args.parse_args()
        result = MemberModel.query.filter_by(memID=member_id).first()
        if result:
            abort(409, message="Member with Member ID {} already exists".format(member_id))
            # 409 is the code for Conflict

        member = MemberModel(memID=member_id, membernumber=args['membernumber'], password=args['password'], fullname=args['fullname'], email=args['email'], phone=args['phone'], address=args['address'], city=args['city'], status=args['status'], paymentstatus=args['paymentstatus'], paymentamount=args['paymentamount'])
        db.session.add(member)
        db.session.commit()
        return member, 201
        # 201 is the code for Created

    @marshal_with(resource_fields)
    def patch(self, member_id):
        args = member_update_args.parse_args()
        result = MemberModel.query.filter_by(memID=member_id).first()

        if not result:
            abort(404, message="Member with Member ID {} doesn't exist".format(member_id))
            # 404 is the code for Not Found

        if args['membernumber']:
            result.membernumber = args['membernumber']
        if args['password']:
            result.password = args['password']
        if args['fullname']:
            result.fullname = args['fullname']
        if args['email']:
            result.email = args['email']
        if args['phone']:
            result.phone = args['phone']
        if args['address']:
            result.address = args['address']
        if args['city']:
            result.city = args['city']
        if args['status']:
            result.status = args['status']
        if args['paymentstatus']:
            result.paymentstatus = args['paymentstatus']
        if args['paymentamount']:
            result.paymentamount = args['paymentamount']

        db.session.commit()

        return result

    def delete(self, member_id):
        result = MemberModel.query.filter_by(memID=member_id).first()

        if not result:
            abort(404, message="Member with Member ID {} doesn't exist".format(member_id))
            # 404 is the code for Not Found

        db.session.delete(result)
        db.session.commit()

        return '', 204
        # 204 is the code for No Content

api.add_resource(Member, '/member/<int:member_id>')

if __name__ == '__main__':
    app.run(debug=True)