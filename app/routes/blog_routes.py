import os
from app.api import datetime, log, parser, resource
import requests
import json

from ..models.blog import Blog
from ..schema.blog_schema import blogs_schema, blog_schema

# from ..plot import Plot

parser.add_argument('title')

class BlogApi(resource):
  def get(self):
    blog = blog.query.filter(blog.active == True)
    result = blog_schema.dump(blog)
    return jsonify(result.data)
