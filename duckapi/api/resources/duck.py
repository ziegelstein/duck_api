from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sqlalchemy.sql import func
from sqlalchemy.orm import load_only
from duckapi.api.schemas import DuckSchema
from duckapi.models import Duck
from duckapi.extensions import db
from duckapi.commons.pagination import paginate

class DuckResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - api
      summary: Get a duck
      description: Get a single duck by ID
      parameters:
        - in: path
          name: duck_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  user: DuckSchema
        404:
          description: Duck does not exists
    put:
      tags:
        - api
      summary: Update a duck
      description: Update a single duck by ID
      parameters:
        - in: path
          name: duck_id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              DuckSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: duck updated
                  duck: DuckSchema
        404:
          description: duck does not exists
    delete:
      tags:
        - api
      summary: Delete a duck
      description: Delete a single duck by ID
      parameters:
        - in: path
          name: duck_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: duck deleted
        404:
          description: duck does not exists
    """

    method_decorators = [jwt_required()]

    def get(self, duck_id):
        schema = DuckSchema()
        duck = Duck.query.get_or_404(duck_id)
        return {"duck": schema.dump(duck)}

    def getRandom(self):
      schema = DuckSchema(many=True)
      query = Duck.query.order_by(func.random()).first()
      return paginate(query, schema)

    def put(self, duck_id):
        schema = DuckSchema(partial=True)
        duck = Duck.query.get_or_404(duck_id)
        duck = schema.load(request.json, instance=duck)

        db.session.commit()

        return {"msg": "duck updated", "duck": schema.dump(duck)}

    def delete(self, user_id):
        duck = duck.query.get_or_404(user_id)
        db.session.delete(duck)
        db.session.commit()

        return {"msg": "duck deleted"}

class DuckList(Resource):
    """Creation and get_all

    ---
    get:
      tags:
        - api
      summary: Get a list of ducks
      description: Get a list of paginated ducks
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/DuckSchema'
    post:
      tags:
        - api
      summary: Create a duck
      description: Create a new duck
      requestBody:
        content:
          application/json:
            schema:
              DuckSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: duck created
                  user: DuckSchema
    """

    method_decorators = [jwt_required()]

    def get(self):
        schema = DuckSchema(many=True)
        query = Duck.query
        return paginate(query, schema)

    def post(self):
        schema = DuckSchema()
        duck = schema.load(request.json)

        db.session.add(duck)
        db.session.commit()

        return {"msg": "Quack.", "duck": schema.dump(duck)}, 201