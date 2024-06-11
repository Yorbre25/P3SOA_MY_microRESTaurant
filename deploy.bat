@REM Primero hacer lo que putas hagan para usar minikube con docker


docker build -t signup Auth/sign_up
docker build -t login Auth/log_in
docker build -t make-admin Auth/make_admin
docker build -t reset-password Auth/reset_password
docker build -t validate-token Auth/validate-token
docker build -t backend-service backend
docker build -t menu-service menu
docker build -t recommendation-service recommendation-service
docker build -t my-reservations reservations
docker build -t sentiment-analysis-service sentiment_analysis



kubectl apply -f .\deployments\sign-up-deployment.yaml   
kubectl apply -f .\deployments\log-in-deployment.yaml   
kubectl apply -f .\deployments\make-admin-deployment.yaml   
kubectl apply -f .\deployments\reset-password-deployment.yaml   
kubectl apply -f .\deployments\validate-token-deployment.yaml   
kubectl apply -f .\deployments\backend-deployment.yaml
kubectl apply -f .\deployments\menu-deployment.yaml
kubectl apply -f .\deployments\recommendation-deployment.yaml
kubectl apply -f .\deployments\reservation-deployment.yaml
kubectl apply -f .\deployments\sentiment-analysis-deployment.yaml

kubectl get pods

kubectl apply -f .\services\sign-up-service.yaml
kubectl apply -f .\services\log-in-service.yaml
kubectl apply -f .\services\make-admin-service.yaml
kubectl apply -f .\services\reset-password-service.yaml
kubectl apply -f .\services\validate-token-service.yaml
kubectl apply -f .\services\backend-service.yaml
kubectl apply -f .\services\menu-service.yaml
kubectl apply -f .\services\recommendation-service.yaml
kubectl apply -f .\services\reservation-service.yaml
kubectl apply -f .\services\sentiment-analysis-service.yaml


@REM minikube service signup-service --url
@REM minikube service login-service --url
@REM minikube service make-admin-service --url
@REM minikube service reset-password-service --url
@REM minikube service validate-token-service --url
@REM minikube service backend-service --url
@REM minikube service menu-service --url
@REM minikube service recommendation-service --url
@REM minikube service reservations-service --url
@REM minikube service sentiment-analysis-service --url

