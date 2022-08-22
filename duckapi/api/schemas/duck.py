from duckapi.models import Duck
from duckapi.extensions import ma, db
from marshmallow import fields


class DuckSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)
    picture_url = fields.Url()
    duckname = ma.String()
    video_url = fields.Url()
    active = ma.Boolean()

    class Meta:
        model = Duck
        sqla_session = db.session
        load_instance = True