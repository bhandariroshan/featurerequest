from settings import db


class FeatureRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(5000))
    client = db.Column(db.String(50))
    client_priority = db.Column(db.Integer())
    target_date = db.Column(db.String(100))
    product_area = db.Column(db.String(100))

    def __init__(self, title, description, client, client_priority, target_date, product_area):
        """

        :param title:
        :param description:
        :param client:
        :param client_priority:
        :param target_date:
        :param product_area:
        """

        self.title = title
        self.description = description
        self.client = client
        self.client_priority = client_priority
        self.target_date = target_date
        self.product_area = product_area

    def __repr__(self):
        return '<Feature Request %r>' % self.title


db.create_all()
db.session.commit()
