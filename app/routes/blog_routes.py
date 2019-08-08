import os
from app.api import datetime, log, parser, Resource, jsonify
import requests
import json

from ..models.blog import Blog
from ..schema.blog_schema import blogs_schema, blog_schema

# from ..plot import Plot

parser.add_argument('title')

class BlogApi(Resource):
  def get(self):
    blog = Blog.query.filter(Blog.active == True)
    result = blog_schema.dump(blog)
    return jsonify(result.data)
