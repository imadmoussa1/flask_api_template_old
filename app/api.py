import os
from datetime import datetime

from flask import Flask
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_restplus import Resource, Api, reqparse
from flask_jwt_extended import (JWTManager, create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from flask_jwt_extended import exceptions as jwt_extended_exceptions
from flask_marshmallow import Marshmallow
from passlib.hash import pbkdf2_sha256

from .config import Config
from .logger import Logger


sha256 = pbkdf2_sha256
log = Logger.log(__name__)
config_env = Config()
datetime = datetime
resource = Resource
parser = reqparse.RequestParser()

db = SQLAlchemy()
bcrypt = Bcrypt()
api = Api()
ma = Marshmallow()


def create_app():
  from .models.user import User
  from .models.blog import Blog
  from .models.revoked_token import RevokedToken

  security = ["basicAuth", "apiKey"]
  authorizations = {
    "basicAuth": {
      "type": "basic",
      "in": "header",
      "name": "Authorization"
    },
    "apiKey": {
      "type": "apiKey",
      "in": "header",
      "name": "Authorization"
    },
  }

  app = Flask(__name__, instance_relative_config=True)

  app.config.update(
    BASEDIR=os.path.abspath(os.path.dirname(__file__)),
    JWT_TOKEN_LOCATION = "headers",
    JWT_SECRET_KEY = config_env.jwt_secret_key(),
    JWT_BLACKLIST_ENABLED = True,
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"],
    SQLALCHEMY_DATABASE_URI = config_env.sqlalchemy_database_uri(),
    SQLALCHEMY_TRACK_MODIFICATIONS = True,
    SECRET_KEY = config_env.secret_key(),
    DEBUG = config_env.debug(),
    PROPAGATE_EXCEPTIONS = True
  )

  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
  # cors = CORS(app, supports_credentials=True)
  jwt = JWTManager(app)

  db.init_app(app)
  ma.init_app(app)
  bcrypt.init_app(app)
  app.app_context().push()

  db.create_all(app=app)
  db.session.commit()

  # import alembic.config
  # from alembic import command
  # alembic_cfg = alembic.config.Config("alembic.ini")
  # command.upgrade(alembic_cfg, "head")

  from .routes.blog_routes import BlogApi
  api.add_resource(BlogApi, '/api/blog')

  from .routes.blog_list_routes import BlogListApi
  api.add_resource(BlogListApi, '/api/blogs')

  # api.init_app(app)
  api.init_app(app=app, authorizations=authorizations, security=security, version="0.0.1", description="REST Template")

  return app
