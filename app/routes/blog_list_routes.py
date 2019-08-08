import os


from app.api import datetime, log, parser, Resource, jsonify
from ..schema.blog_schema import blogs_schema
from ..models.blog import Blog

class BlogListApi(Resource):
  def get(self):
    blogs = Blog.query.filter(Blog.active == True)
    result = blogs_schema.dump(blogs)
    return jsonify(result.data)