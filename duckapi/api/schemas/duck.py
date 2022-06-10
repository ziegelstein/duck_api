from duckapi.models import Duck
from duckapi.extensions import ma, db


class DuckSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)

    class Meta:
        model = Duck
        sqla_session = db.session
        load_instance = True
        exclude = ("_password",)