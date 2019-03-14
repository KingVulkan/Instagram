# Instagram

This is an Instagram app clone

## Author

Abdulrahman Abdullahi Omar

## Setup/Installation Requirements

Python version should be 3.6 -Django version 1.11 pip install django==1.11

Additionally, you’ll need to make sure you have pip available. You can check this by running:
```
pip --Version
Install Pipenv pip install --user pipenv
install virtualenv and then test it
python3.6 pip install --user --upgrade pip
python3.6 -m virtualenv env
source env/bin/activate
```
Inorder to clone , follow the procedure below;

On GitHub, navigate to the main page of the repository.

Under the repository name, click Clone or downlonload.

click the paste button.

Open Terminal.

Change the current working directory to the location where - you want the cloned directory to be made.

Type git clone, and then paste the URL you copied in Step 2 Press Enter.


## Psql

CREATE DATABASE instagram

connect to the database \c instagram

check if tables have been created \dt


## Run migrations

python3.6 manage.py migrate

python3.6 manage.py makemigrations gram

## Running the app

python3.6 manage.py runserver

## Testing

python3.6 manage.py test gram


## Behaviour driven development

| Behaviour   |      Input     |  Output |
|----------|:-------------:|------:|
| User Sign In | Enter user details on sign in page |   Account and profile created |
| Edit profile | Click "Edit profile" button on profile page |   Enter details |
| User Log In | Enter user details on log in page |   User redirected to the profiles page upon successful log in |
| Follow other users | Visit profiles page |   Click "follow" button |
| Display Images | Visit the timeline page |   User can view Images in cronological order |
| Like Image | Click on the "heart shaped" icon at the bootom of a picture |   Like is recorded |
| Expand Image | Click on image |   Expanded Image on an individual page |
| View More Details | Expand Image |  More details appear on the right side of the expanded image |


## Technologies Used

HTML

CSS

Python

Django

Postgres

javascript

## Known Bugs

The website does not function well on explorer and heroku

## License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE Copyright (c) {2018} {By Abdulrahman Abdullahi}
