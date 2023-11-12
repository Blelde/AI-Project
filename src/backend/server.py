# backend/server.py
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use a proper database URL
db = SQLAlchemy(app)
api = Api(app)

# Register API resources
api.add_resource(ClusteringAPI, '/api/clustering')
api.add_resource(VisualizationAPI, '/api/visualization')

if __name__ == '__main__':
    app.run(debug=True)
