# P3SOA_MY_microRESTaurant

minikube start
$Env:DOCKER_TLS_VERIFY = "1"
$Env:DOCKER_HOST = "tcp://127.0.0.1:60685"
$Env:DOCKER_CERT_PATH = "C:\Users\lazh\.minikube\certs"
$Env:MINIKUBE_ACTIVE_DOCKERD = "minikube"
& minikube -p minikube docker-env --shell powershell | Invoke-Expression


kubectl apply -f



https://stackoverflow.com/questions/38979231/imagepullbackoff-local-repository-with-minikube


PS C:\TEC\2024_S1\SOA\Proyecto4\P3SOA_MY_microRESTaurant> minikube service menu-service --url
http://127.0.0.1:53507
❗  Because you are using a Docker driver on windows, the terminal needs to be open to run it.



Guia Minikube 

minikube start # empieza el minikube
& minikube -p minikube docker-env --shell powershell | Invoke-Expression # setea el docker al interno de minikube, debe correrse en powershell


Guia para agregar o actualizar un servicio
Realizar los cambios en el codigo
docker build -t nombre_servicio:tag # crear nuevamente la imagen
kubectl get pods # devuelve todas las pods
kubectl delete <todas las pods del servicio a actualizar>
kubectl get pods # verifica que se hayan creado nuevamente y que el AGE sea muy reciente
minikube service menu-service --url #mapeo el servicio a una ip de la compu para pruebas
