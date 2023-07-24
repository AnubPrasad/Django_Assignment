# Django_Assignment
Customizing Artist API

### Installation Instructions:  
[I am used postman for api call.](https://www.postman.com/downloads/)
  
### Install Django:
pip install django


## Create and activate a virtual environment (recommended):

### Create a virtual environment
python -m venv env

## Activate the virtual environment
### Windows:
env\Scripts\activate
  
### macOS/Linux:
source env/bin/activate


**Project Setup:**  
Clone the repository:

git clone https://github.com/sleep323/Django_Assignment.git  
cd your-repo

Run the Django Development Server:
python manage.py runserver
Your project will now be accessible at http://localhost:8000/.

### Token-Based Authentication:
Users can register an account by making a POST request to /accounts/api/register/.  
Users can login and retrieve their authentication token by making a POST request to /accounts/api/login/.


### Rest API Endpoints:  
**Create a new work:**  
Endpoint: POST /accounts/api/works/new_works/  
Request Body: JSON data with work details  

**Retrieving a list of all works:**  
Endpoint: GET /accounts/works/

**Integrate Filtering with Work Type:**  

Endpoint:   GET /api/works/?work_type=<work_type>  
Replace <work_type> with the desired work type (e.g., "YT", "IG", "OT").   

### Apply database migrations before running the server:  
**python manage.py makemigrations  
python manage.py migrate**  


### Deploying to Production (Optional):  
If you want to deploy your Django project to a production environment, consider using platforms like Heroku, AWS, or DigitalOcean.  
### Additional Notes:  
You can customize the project as per your requirements and add more API endpoints or features.

