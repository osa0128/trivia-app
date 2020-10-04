Full Stack Trivia API Backend
Getting Started
Installing Dependencies
Python 3.7

Follow instructions to install the latest version of python for your platform in the python docs
Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs
PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:

pip install -r requirements.txt

This will install all of the required packages we selected within the requirements.txt file.
Key Dependencies

    Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

    SQLAlchemy is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

    Flask-CORS is the extension we'll use to handle cross origin requests from our frontend server.

Database Setup

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

psql trivia < trivia.psql

Running the server

From within the backend directory first ensure you are working using your created virtual environment.

To run the server, execute:

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run

Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.

Setting the FLASK_APP variable to flaskr directs flask to use the flaskr directory and the __init__.py file to find the application.
Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

    Use Flask-CORS to enable cross-domain requests and set response headers.
    Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
    Create an endpoint to handle GET requests for all available categories.
    Create an endpoint to DELETE question using a question ID.
    Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score.
    Create a POST endpoint to get questions based on category.
    Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
    Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
    Create error handlers for all expected errors including 400, 404, 422 and 500.

Endpoints GET '/categories' GET ... POST ... DELETE ...
API

GET '/categories'

    Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
    Request Arguments: None
    Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.

{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}

GET '/questions?page=(page number)'

    Fetches a paginated dictionary of questions of all category
    Request Arguments (optional): page number

{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "success": true, 
  "total_questions": 19
}

DELETE '/questions/int:question_id'

    Delete a questions
    Request Arguments: question_id

{
    'success': True,
    'deleted_question':question_id
}

POST '/questions'

    Post a new Question to specific category
    Request Date: [question:string, answer:string, difficulty:int, category:string]

{
    'success': True,
    'total_questions':len(selection)
}

POST '/questions/searchresult'

    Post a new search for a specific questions
    Request Date: SearchTerm:string

{
  "current_category": null, 
  "questions": [
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }
  ], 
  "success": true, 
  "total_questions": 1
}

GET '/categories/int:category_id/questions'

    GET all questions for specific category
    Request Arguments: int:category_id

{
  "current_category": 4, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Scarab", 
      "category": 4, 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ], 
  "success": true, 
  "total_questions": 4
}

POST '/quizzes'

    Post a new quiz with random questions with no dublicated questions
    Request Date: array:previous_questions, quiz_category: int:id

{
  "question": 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
  "success": true
}

Testing

To run the tests, run

dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
