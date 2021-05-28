import webapp

if __name__ == '__main__':
    webapp.db.init_app(webapp.app)
    with webapp.app.app_context():
        webapp.db.create_all()
    webapp.app.run(debug=True, port=8000)