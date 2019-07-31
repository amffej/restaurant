# QuickChat - Simple chat application


## Objective

The goal of this project was to build a web application that handlls a pizza restaurant’s online orders. Users have the ability to browse the restaurant’s menu, add items to their cart, and submit their orders. Meanwhile, the restaurant owners can to to and update menu items, view orders that have been placed and mark them as complete. For this project the framework used was Django.

### Login Information

```
Administrator
    user:admin
    pass:admin

Test User
    user:testuser
    pass:testpassword
```


### File Structure

```
project3-jeffmaldo27/
├── orders/           # app folder  
│   ├── admin.py      # Register models to show on admin page
│   ├── apps.py       # Apps configuration
│   ├── forms.py      # Used to for expanded registration form
│   ├── models.py     # Registerd all app models here
│   ├── tests.py      # No tests registered here
│   ├── urls.py       # all of the urls were configured here
│   ├── views.py      # All of the definitions were configured here
│   └── templates/    # App template folder
│       ├── orders/
│       │       ├── base.html           # main template
│       │       ├── cart.html           # cart template
│       │       ├── category.html       # cartegory display template
│       │       ├── index.html          # homepage template
│       │       ├── item.html           # item template
│       │       ├── orders.html         # order template
│       │       └── orders_admin.html   # admin orders template
│       └── registration/
│               ├── login.html          # login template
│               └── register.html       # register template           
├── pizza/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore          # gitignore configurations
├── db.sqlite3          # Local database file
├── README              # this file
├── requirements.txt    # Install requirements


│   ├── img/
│   │   └──  app.png    # Image used in readme
│   ├── index.js        # Main JavaScript File for the chat
│   └── style.css       # Custom CSS file
├── application.py      # Main flask application file
├── README.md           # This file!
├── .gitignore          # Git ignore configuration file
└── requirements.txt    # List required packages
```

### Features

* Single page design - All content is loaded within one main page (Personal Touch)
* Mobile friendly - Automatically hide channels on mobile view. (Personal Touch)
* Unread message counters - Badge showing unread messages per channel (Personal Touch)
* Save up to 100 messages per channel
* User can create custom channels
* No need to sign in again if browser is closed