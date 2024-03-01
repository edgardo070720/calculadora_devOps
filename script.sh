

docker login -u edgardo07

# Etiqueta tu imagen con el formato nombre_de_usuario/nombre_del_repositorio:etiqueta
docker tag prueba edgardo07/calculadora:1.0


# Sube la imagen al registro público
docker push edgardo07/calculadora:1.0
