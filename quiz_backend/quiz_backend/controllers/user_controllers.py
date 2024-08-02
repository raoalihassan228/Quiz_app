from quiz_backend.utils.imports import (Token, User, UserModel, Session, select, passwordIntoHash)

def signUp(user_form:UserModel, session:Session):
    user_exist = session.exec(select(User).where(User.user_email == user_form.user_email))
    if user_exist:
        raise
    hashed_password= passwordIntoHash(user_form.user_password)
    user = User(user_name=user_form.user_name, user_email=user_form.user_email, user_password=hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)