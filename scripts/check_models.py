import mlflow
from mlflow.tracking import MlflowClient

# Point to your remote MLflow tracking server
mlflow.set_tracking_uri("http://ec2-13-200-250-45.ap-south-1.compute.amazonaws.com:5000/")

client = MlflowClient()

# Try listing models (works across versions)
try:
    models = client.list_registered_models()
except AttributeError:
    models = client.search_registered_models()

print("Models found in registry:")
for m in models:
    print("-", m.name)

# Check latest versions and stages for your model
model_name = "yt_chrome_plugin_model"
try:
    versions = client.get_latest_versions(model_name)
    print(f"\nLatest versions for model '{model_name}':")
    for v in versions:
        print(f"  Version {v.version}, Stage: {v.current_stage}, Run ID: {v.run_id}")
except Exception as e:
    print(f"Error fetching versions for '{model_name}': {e}")
