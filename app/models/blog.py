from app.api import db, datetime
from sqlalchemy_utils import IPAddressType


class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(240), unique=True, nullable=False)
    description = db.Column(db.String(240), nullable=False)
    content = db.Column(db.String(240), nullable=False)
    # ip_address = db.Column(IPAddressType)
    active = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
    added_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    user = db.relationship("User")

    def __init__(self, title=None, description=None, content=None, active=None, updated_at=None):
        self.hash = hash
        self.title = title
        self.description = description
        self.content = content
        self.active = active

        if updated_at is None:
            self.created_at = datetime.now()
        else:
            self.updated_at = updated_at
        # self.added_by = None if current_user.is_anonymous else current_user.id
