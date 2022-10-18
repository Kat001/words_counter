from datetime import date
import sqlalchemy_jsonfield
from words_scrapper import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username} ', '{self.email}', '{self.image_file}')"


class PageWordsCount(db.Model):
    """
    This model will store all the deatils related to url
    and counting of words.
    """ 
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=date.today(), nullable=False) 
    url = db.Column(db.String())
    total_words = db.Column(db.Integer())
    json_record = db.Column(
        sqlalchemy_jsonfield.JSONField(
            # MariaDB does not support JSON for now
            enforce_string=True,
            # MariaDB connector requires additional parameters for correct UTF-8
            enforce_unicode=False
        ),
    )

 
    def __init__(self, url,total_words,json_record):
        self.url = url
        self.total_words = total_words
        self.json_record = json_record
 
    def __repr__(self):
        return f"{self.url}"

