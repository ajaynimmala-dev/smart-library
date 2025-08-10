from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    user_role = db.Column(db.String, default="student", nullable=False)
    mobile_number = db.Column(db.Numeric(10), nullable=True)

    def is_user_valid(self,email,password)->bool:
        check_email = User.query.filter_by(email=email).first()
        if check_email:
            return True if check_email.password_hash == password else False
        return False