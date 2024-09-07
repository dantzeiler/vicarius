def setup_routes(app):
    # Define a route for the homepage
    @app.route('/')
    def home():
        return "Welcome to my Flask website! haha"

    # Define a route for a contact page
    @app.route('/contact')
    def contact():
        return "Contact us at: contact@example.com"
