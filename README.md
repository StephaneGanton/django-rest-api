# django-rest-api-shopping-api
A project to develop an **API** for **ecommerce plateform** in order to go through the main basics of `Django Rest Framework`

## Motivation

This project is part of a serie of projects we build to get dive into **Django web Framework**.
It  can be found through [Free Code camp website](https://www.youtube.com/watch?v=Yg5zkd9nm6w)

## Keys Takeaways

Going through this projects helps us understand:   
 
- authentication
- register and retrive images from db using [pillow package](https://pillow.readthedocs.io/en/stable/)
- Integration of [Stripe](https://stripe.com/) for payment
- Deployment to server


## Deployment

To launch this project after cloning it, run:

- Create and activate a virtual environment:
    
```bash
    virtualenv <name>

    source <name>/bin/activate
```

- Install dependencies:
    ```bash
        pip install -r requirements.txt
    ```
- Run migrations:
```bash
    python manage.py makemigrations 

    python manage.py migrate 
```
- Run server:
```bash
    python manage.py runserver

