from sqlalchemy.ext.hybrid import hybrid_property

from duckapi.extensions import db, pwd_context


class Duck(db.Model):
    """Basic duck model"""

    id = db.Column(db.Integer, primary_key=True)
    duckname = db.Column(db.String(80), unique=True, nullable=False)
    picture_url = db.Column(db.String(256), unique=True, nullable=False)
    video_url = db.Column(db.String(256), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<duck %s>" % self.duckname