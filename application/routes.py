#routes file
def setup_routes(app):
    # Define a route for the homepage
    @app.route('/')
    def home():
        return "Welcome to my Flask website! haha"

    # Define a route for API pods
    @app.route('/pods/kube-system', methods=['GET'])
    def get_pods():
        try:
            v1 = client.CoreV1Api()
            pods = v1.list_namespaced_pod(namespace='kube-system')
            pod_list = [{"name": pod.metadata.name, "status": pod.status.phase} for pod in pods.items]
            return jsonify(pod_list), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

