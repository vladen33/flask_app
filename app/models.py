from . import db


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return dict(
            id = self.id,
            title = self.title,
            text = self.text
        )

    def from_dict(self, data):
        for field in ['title', 'text']:
            print('field = ', field)
            if field in data:
                setattr(self, field, data[field])