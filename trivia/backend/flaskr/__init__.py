import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import sys
from werkzeug.datastructures import Headers

from models import setup_db, Question, Category



QUESTIONS_PER_PAGE = 10

def paginate_questions(request,selection):
      page = request.args.get('page', 1, type=int)
      start = (page - 1) * QUESTIONS_PER_PAGE
      end = start + QUESTIONS_PER_PAGE
      questions = [question.format() for question in selection]
      current_question = questions[start:end]
      return current_question




def create_app():
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)




  CORS(app)
 
  
  @app.after_request
  def after_request(response):
        response.headers["Access-Control-Allow-Origin"] = "*",
        response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true'),
        response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS')

        return response
  

  @app.route('/')
  def index():
        return '''i am here don't worried'''
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def categories():
      try:

            categories = Category.query.all()
            
           
            category = {category.id: category.type for category in categories}
            return jsonify({
                  'success' : True,
                  'categories' : category
            })
      except:
            abort(404)

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 
  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions')
  def questions():

      try:
         selection = Question.query.order_by(Question.id).all()
         current_questions = paginate_questions(request, selection)
         
         categories = Category.query.all()

         if len(current_questions) == 0:
            abort(404)
            
         return jsonify({
               'success': True,
               'questions': current_questions,
               'total_questions': len(selection),
               'categories': {category.id: category.type for category in categories},
               'current_category': None
         })
      except:
         abort(404)



  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID.
  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/question/<int:question_id>', methods = ['DELETE'])
  def delete_question(question_id):
        try:
            question = Question.query.get(question_id)
            question.delete()
            return jsonify({
                  'deleted': question_id,
                  'success': True
            })
        except:
              abort(422)
 


  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.
  '''
  @app.route('/questions', methods=['POST'])
  def add_question():
      try:
            body = request.get_json()
            if not ('question' in body and 'answer' in body and 'difficulty' in body and 'category' in body):
                abort(422)
            add_question = body.get('question')
            add_answer = body.get('answer')
            add_difficulty = body.get('difficulty')
            add_category = body.get('category')
              
            new_question = Question(question=add_question, answer=add_answer, difficulty=add_difficulty, category=add_category)
            new_question.insert()

            return jsonify({
                  'success': True,
                  'created': new_question.id
            })
      except:
            abort(422)
  



  '''
  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 
  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions/search', methods=['POST'])
  def questions_search():
      try:  
        body = request.get_json()
        search_term = body.get('searchTerm')
      
        results =  Question.query.filter(Question.question.ilike('%{}%'.format(search_term))).all()
        return jsonify({
              'success': True,
              'questions': [question.format() for question in results],
              'total_questions': len(results),
              'current_category':None

        })
      except:
        abort(500)



  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 
  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def category_question(category_id):
      try:
        questions = Question.query.filter(Question.category == str(category_id)).all()
       
        return jsonify({
              'success': True,
              'questions': [question.format() for question in questions],
              'totalQuestions': len(questions),
              'currnetCategory': category_id

        })
      except:
         abort(500)

  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def play_quiz():

        try:

            body = request.get_json()

            if not ('quiz_category' in body and 'previous_questions' in body):
                abort(422)

            category = body.get('quiz_category')
            previous_questions = body.get('previous_questions')

            if category['type'] == 'click':
                available_questions = Question.query.filter(
                    Question.id.notin_((previous_questions))).all()
            else:
                available_questions = Question.query.filter_by(
                    category=category['id']).filter(Question.id.notin_((previous_questions))).all()

            new_question = available_questions[random.randrange(
                0, len(available_questions))].format() if len(available_questions) > 0 else None

            return jsonify({
                'success': True,
                'question': new_question
            })
        except:
            abort(422)
  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
        return jsonify({
              'success': False,
              'error':404,
              'message':"Not Found"
        }), 404


  @app.errorhandler(422)
  def unprocessable_entity(error):
        return jsonify({
              'success': False,
              'error':422,
              'message':"Unprocessable Entity"
        }), 422

  @app.errorhandler(500)
  def server_error(error):
        return jsonify({
              'success': False,
              'error':500,
              'message':"internet server error"
        }), 500
  
  
  @app.errorhandler(400)
  def Bad_request(error):
        return jsonify({
              'success': False,
              'error':400,
              'message':"Bad request"
        }), 400
  return app
    
