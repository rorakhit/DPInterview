========================
HelloCrypto Application
========================

Author: Rohini Rakhit

HelloCrypto is an application that will take your csv input and output a line chart displaying your data.

To run the application:
1. create a postgres database called 'helloCrypto'
2. create a virtualenv
3. go to pyenv.cfg inside the virtualenv and change include-system-site-packages to true
4. activate the virtualenv
5. navigate to django-helloCrypto/
6. pip install .
7. navigate ../helloCrypto
8. run ``python3 manage.py migrate`` to create the models for helloCryptoApp
9. run ``python3 manage.py runserver`` to run the development server and 
10. navigate to http://localhost:8000/helloCryptoApp/index to upload your csv.

Note: I got the redirect and the data in the right format to be output as a line chart, but I couldn't get the line chart to show up on the screen.
I've inspected and it looks like the canvas is showing up just fine it's just the image isn't showing up in the canvas object.
