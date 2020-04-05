from application import db

class Prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prize = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return ''.join(['ID: ', str(self.id), '\r\n', 'Prize: ', str(self.prize)])
