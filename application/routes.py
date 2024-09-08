#routes file
def setup_routes(app):
    # Define a route for the homepage
    @app.route('/')
    def home():
        return "Welcome to my Flask website! haha"

    # Define a route for API pods
    @app.route('/pods', methods=['GET'])
    def get_pods():
        v1 = client.CoreV1Api()
        namespace = 'kube-system'
        try:
            pods = v1.list_namespaced_pod(namespace)
            pod_list = [pod.metadata.name for pod in pods.items]
            return jsonify({'pods': pod_list}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

