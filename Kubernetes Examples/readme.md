# Setting up the Cluster

### After creating the cluster, run the following command in the Cloud Shell to get credentials:
``` 
gcloud container clusters get-credentials sample-cluster --zone europe-west3
```

### Pre-built Image:
``` 
tiangolo/uwsgi-nginx-flask:python3.8
```

### Create a Namespace:
``` 
kubectl create namespace test
kubectl config set-context --current --namespace=test
```

### Apply the Manifests:
``` 
kubectl apply -f flask-app-deployment.yaml
kubectl apply -f flask-app-service.yaml
```

### Summary:
1. You have a GKE cluster named sample-cluster.
2. You’ve connected to it using the gcloud command so that kubectl can talk to it directly.
3. You created a separate namespace test for logical grouping and to avoid resource name conflicts.
4. You applied the provided manifests which define a Deployment (to run the Flask pods) and a Service (to expose them internally or externally).
