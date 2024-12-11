from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from db import connect_db, create_table, insert_user, get_all_users

app = FastAPI()

# Example User model
class User(BaseModel):
    name: str
    age: int

conn = connect_db()
create_table(conn)

# POST request to create a new user
@app.post("/users/")
def create_user(user: User):
    user_id = insert_user(conn, user.name, user.age)
    return {"id": user_id, "name": user.name, "age": user.age}

# GET request to retrieve all users
@app.get("/users", response_model=List[User])
def get_all_users_api():
    users = get_all_users(conn)
    return users

# Run the FastAPI application
#if __name__ == "__main__":
#    import uvicorn

#    uvicorn.run(app, host="0.0.0.0", port=8000)


#from fastapi import FastAPI

#app = FastAPI()

# GET request for the root route
@app.get("/")
async def read_root():
    return {"message": "Hello,Taha Shahid aj tumne konse rang ke mooze phene hain?"}

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

