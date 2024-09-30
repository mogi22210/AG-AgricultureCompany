import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'adm')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', '1234')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'prueba1')
TEST_DATABASE_NAME = os.getenv('DATABASE_NAME', 'prueba1_test')
