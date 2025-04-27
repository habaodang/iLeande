from leande.model import Account
from leande import db
from leande import login_manager

def add_account(name,password):
    acc=Account(name=name,password=password)

    db.session.add(acc)
    db.session.commit()

def login(name,password):
    acc = Account.query.filter(Account.name == name, Account.password == password).first()

    if not acc:
        return False
    return acc

# Định nghĩa user_loader
@login_manager.user_loader
def load_user(user_id):

    # Tìm người dùng trong cơ sở dữ liệu dựa trên user_id
    return Account.query.get(int(user_id))
