# Cluster'ı Kur

# Cluster Açtıktan Sonra Cloud Shell üzerinden; 
gcloud container clusters get-credentials sample-cluster --zone europe-west3 

# Hazır Image: tiangolo/uwsgi-nginx-flask:python3.8

# NameSpace Aç

kubectl create namespace test
kubectl config set-context --current --namespace=test

# Manifestleri yolla
kubectl apply -f flask-app-deployment.yaml
kubectl apply -f flask-app-service.yaml
