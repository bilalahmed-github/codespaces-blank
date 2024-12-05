from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Example User model
class User(BaseModel):
    id: int
    name: str
    age: int

# Example in-memory user database
database: Dict[int, User] = {}

# GET request to retrieve a user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in database:
        raise HTTPException(status_code=404, detail="User not found")
    return database[user_id]

# POST request to create a new user
@app.post("/users/")
def create_user(user: User):
    if user.id in database:
        raise HTTPException(status_code=400, detail="User already exists")
    database[user.id] = user
    return user

# PUT request to update an existing user
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    if user_id not in database:
        raise HTTPException(status_code=404, detail="User not found")
    database[user_id] = updated_user
    return updated_user

# DELETE request to remove a user by ID
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in database:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = database.pop(user_id)
    return {"message": "User deleted successfully", "deleted_user": deleted_user}

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
