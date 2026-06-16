from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str


def greet_user(user: User) -> str:
    return f"Hello! {user.name}"


def load_data(data: User):
    return User.model_validate(data)


user = load_data({"name": "Alice", "email": "alice@example.com"})
message = greet_user(user)
print(message)
