from server.app import db

class Restaurant(db.model):
    __tablename__ = 'restaurants'

    id = db.column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    restaurant_pizzas = db.relationship()


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address":self.address
        }