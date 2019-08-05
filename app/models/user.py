from app.api import db, bcrypt, datetime, sha256


class User(db.Model):

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
  user_name = db.Column(db.String(120), nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=True)
  authenticated = db.Column(db.Boolean, default=False)
  registered_on = db.Column(db.DateTime, nullable=True)
  is_admin = db.Column(db.Boolean, nullable=False)

  def __init__(self, email, plaintext_password):
    self.email = email
    self.authenticated = False
    self.registered_on = datetime.now()
    self.role = role

  def get_id(self):
    """Return the id of a user to satisfy Flask-Login's requirements."""
    return str(self.id)

  def __repr__(self):
    return '<User {}>'.format(self.email)

  @classmethod
  def find_by_username(cls, username):
    return cls.query.filter_by(userName=username).first()

  @staticmethod
  def generate_hash(password):
    return sha256.hash(password)

  @staticmethod
  def verify_hash(password, hash):
    return sha256.verify(password, hash)
