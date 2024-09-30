from flask import Flask, jsonify
from kubernetes import client, config

app = Flask(__name__)

# Load Kubernetes configuration
config.load_incluster_config()


@app.route('/')
def home():
    return "Welcome to Dans Landing page\n Alex smells like bacon!!! to get more pod info please process to the '/pods' page"


@app.route('/pods', methods=['GET'])
def get_pods():
    try:
        v1 = client.CoreV1Api()
        pods = v1.list_namespaced_pod(namespace='kube-system')
        pod_list = [{"name": pod.metadata.name, "status": pod.status.phase} for pod in pods.items]
        return jsonify(pod_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
