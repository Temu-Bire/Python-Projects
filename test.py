# from pydantic import BaseModel

# class User(BaseModel):
#     id: int
#     name: str
#     age: int|None = None
#     is_active: bool=True

# user = User(id="1", name='Alice', age=30)
# print(user.model_dump())
# print(user.model_dump_json(indent=4))
# try:
#     bad=User(id="abc", name='Bob', age='twenty')
# except Exception as e:
#     print(e)

# from pydantic import BaseModel, Field, EmailStr, ValidationError
# class Product(BaseModel):
#     id: int = Field(..., gt=0)
#     name: str=Field(..., min_length=3, max_length=100)
#     price: float = Field(..., gt=0, description="Price must be greater than zero")
#     email: EmailStr|None=None
# try:
#     product = Product(id=1, name='Laptop', price=999.99, email='alice@example.com')
#     print(product.model_dump())
# except ValidationError as e:
#     print(e)

# from pydantic import BaseModel
# class CreateOrder(BaseModel):
#     customer_id: int
#     item: list[dict[str, int]]
#     shipping_address: str
#     total_price: float
# order_data = {
#     "customer_id": 123,
#     "item": [{"product_id": 1, "quantity": 2}, {"product_id": 2, "quantity": 1}],
#     "shipping_address": "123 Main St, Anytown, USA",
#     "total_price": 49.99
# }
# order=CreateOrder.model_validate(order_data)
# print(order.model_dump())   



#nested model
# from pydantic import BaseModel, Field
# class Address(BaseModel):
#     street: str
#     city: str
#     zip_code: str
# class User(BaseModel):
#     id: int
#     name: str
#     age: int|None = None
#     is_active: bool=True
#     address: Address
# user_data = {
#     "id": 1,
#     "name": "Alice",
#     "age": 30,
#     "is_active": True,
#     "address": {
#         "street": "123 Main St",
#         "city": "Anytown",
#         "zip_code": "12345"
#     }}
# user = User.model_validate(user_data)
# print(user.model_dump())


# from pydantic import BaseModel, Field
# from streamlit import json
# class Author(BaseModel):
#     name: str
#     age: int|None = None
# class Book(BaseModel):
#     title: str
#     page: int=Field(..., gt=0)
#     isbn: str=Field(..., min_length=13, max_length=13)
#     Author: Author
# book_data = {
#     "title": "The Great Gatsby",
#     "page": 180,
#     "isbn": "1234567890123",
#     "Author": {
#         "name": "F. Scott Fitzgerald",
#         "age": 44
#     }
# }
# book = Book.model_validate(book_data)
# print(book.model_dump())

from numpy import number
from pydantic import BaseModel, Field
class Computer(BaseModel):
    brand: str=Field(..., min_length=2, max_length=50, description="Brand name must be between 2 and 50 characters",)
    model: str=Field(..., min_length=2, max_length=100)
    price: float=Field(..., gt=0)
class Labratory(BaseModel):
    name: str=Field(..., min_length=2, max_length=100)
    location: str=Field(..., min_length=2, max_length=100)
    number_of_computers: int=Field(..., gt=0)
    computers: list[Computer]
lab_data = {
    "name": "Tech Lab",
    "location": "Building A",
    "number_of_computers": 2,
    "computers": [
        {"brand": "Dell", "model": "XPS 15", "price": 1500.00},
        {"brand": "Apple", "model": "MacBook Pro", "price": 2000.00}
    ]
}
lab = Labratory.model_validate(lab_data)
print(lab.model_dump())