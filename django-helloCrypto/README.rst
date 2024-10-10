========================
HelloCrypto Application
========================

HelloCrypto is an application that will take your csv input and output a line chart displaying your data.

To run the application:
1. create a posgres database called 'helloCrypto'
2. add "helloCryptoApp" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'helloCryptoApp',
    ]
3. Include the polls URLconf in your project urls.py like this::

    path('polls/', include('polls.urls')),
4. Run ``python3 manage.py migrate`` to create the models for helloCryptoApp
5. Run ``python3 manage.py runserver`` to run the development server and navigate to http://localhost:8000/helloCryptoApp/index to upload your csv.
