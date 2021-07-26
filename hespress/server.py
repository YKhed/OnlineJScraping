from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class ArticleModel(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    Url = db.Column(db.String(500), nullable=False)
    Title = db.Column(db.String(200), nullable=False)

    def __repr__(self) :
        return "Article(Url = {0}, Title = {1})".format(ArticleModel.Url,ArticleModel.Title)

resource_fields = {
    'id' : fields.Integer,
    'Url' : fields.String,
    'Title' : fields.String
}

article_put_args = reqparse.RequestParser()
article_put_args.add_argument("Url", type=str, help="Article url is required", required=True)
article_put_args.add_argument("Title", type=str)


class Article(Resource) :
    @marshal_with(resource_fields)
    def put(self, article_id) :
        args = article_put_args.parse_args()
        result = ArticleModel.query.filter_by(id=article_id).first()
        if result :
	        abort(409, message="Article id taken.")
        article = ArticleModel(id = article_id, Url=args["Url"], Title=args["Title"])
        db.session.add(article)
        db.session.commit()
        return article, 201

    @marshal_with(resource_fields)
    def get(self, article_id) :
        result = ArticleModel.query.filter_by(id=article_id).first()
        if not result:
	        abort(404, message="Could not find an article with that id.")
        return result


api.add_resource(Article, "/article/<int:article_id>")

if __name__ == "__main__" :
    app.run(debug=True)   # debug=True only when developing for testing purposes 

