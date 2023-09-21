from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = "authors"
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("name")
    def validate_name(self, key, name):
        if not name:
            raise ValueError("No name provided")

    @validates("phone_number")
    def validate_number(self, key, phone_number):
        if len(phone_number) > 10:
            raise ValueError("Phone number must be 10 digits long")

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name})"


class Post(db.Model):
    __tablename__ = "posts"
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("title")
    def validate_title(self, key, title):
        if not title:
            raise ValueError("All posts must have a title")
        valid_clickbait = ["Won't Beleive", "Secret", "Top", "Guess"]
        if title not in valid_clickbait:
            raise ValueError("NOT CLICKBAITY ENOUGH")

    @validates("content")
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError("All content must be at least 250 characters long")

    @validates("summary")
    def validate_summary(self, key, summary):
        if len(summary) >= 250:
            raise ValueError("All summaries must be no longer than 250 characters long")

    @validates("category")
    def validate_category(self, key, category):
        valid_categories = ["Fiction", "Non-Fiction"]
        if category not in valid_categories:
            raise ValueError("All categorires must be either Fiction or Non-Fiction")

    # @validates('title')
    # def validates_clickbait(self, key, title):
    #     valid_clickbait = ["Won't Beleive", "Secret", "Top", "Guess"]
    #     if title not in valid_clickbait:
    #         raise ValueError("NOT CLICKBAITY ENOUGH")

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})"
