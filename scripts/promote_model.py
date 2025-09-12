import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://ec2-13-200-250-45.ap-south-1.compute.amazonaws.com:5000/")
client = MlflowClient()

# Change version number if needed
client.transition_model_version_stage(
    name="yt_chrome_plugin_model",
    version=6,
    stage="Staging"
)

print("✅ yt_chrome_plugin_model version 6 promoted to Staging")
