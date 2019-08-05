import os
from app.api import datetime, log, parser, resource
import json
from ..schema.blog_schema import blogs_schema
from ..models.blog import Blog

class BlogListApi(resource):
  def get(self):
    blogs = blog.query.filter(blog.active == True)
    result = blogs_schema.dump(blogs)
    return jsonify(result.data)