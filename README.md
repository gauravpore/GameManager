# 🔹Game Manager CRUD APIs 🎮
## 🌐 Deployed Project Link --> [https://gforce.pythonanywhere.com/swagger/](https://gforce.pythonanywhere.com/swagger/)

## 🔸Overview:
Game Manager APIs are CRUD apis that'll allow us to manage CRUD operation on Game object in database.

## 🔸**Concepts:**
- API Development
- Django Development
- CRUD Operations
- Deployment
- Project Management

## 🔸**Tools & Technologies:**
- Python 3
- [Django](https://www.djangoproject.com/start/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Postman API Platform](https://learning.postman.com/docs/getting-started/introduction/)
- Swagger
- Requests
- Sqlite3
- Git 
- VS Code

### 🔸**API overview:**
```
1. ```/api/create-game``` -> Creates a new game object in database using django ORM with the provided params (name, url, author, published_date). 
2. ```/api/read-game``` -> Retrieves single specific game data based on `game_id` or `name` of the game.
3. ```/api/get-all-games``` -> Retrieves data of all games stored in database.
4. ```/api/update-game``` -> Updates Game with all the provided request data.
5.  ```/api/delete-game``` -> Deletes entire Game object matching with given `game_id`.
```
