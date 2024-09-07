def setup_routes(app):
    # Define a route for the homepage
    @app.route('/')
    def home():
        return "Welcome to my Flask website! haha"

    # Define a route for API pods
    @app.route('/pods')
    def contact():
        return "Contact us at: contact@example.com"
