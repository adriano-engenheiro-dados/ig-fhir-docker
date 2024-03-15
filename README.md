# Ambiente para fhir/ig utilizando docker

## Requisitos mínimos:
Docker instalado e executando. Docker compose instalado.

## Resumo
Este é um projeto modificado do colaborador Murilo (https://github.com/muriloluz/fhir-ambiente) para ser executado diretamente no Docker Compose. É um projeto em andamento, para facilitar o Deploy do projeto em um ambiente Kubernetes.

## Exemplo execução

A partir do diretório docker executar:

`docker compose up`

Essa instrução cria a imagem guia-implementacao-sesgo em sua versão mais recente, com os requisitos para execução de um exemplo do Guia de implementação.

A imagem também disponibiliza o apache para visualização da aplicação web gerada.

Observe que houve um direcionamento de porta do host para o container (80:80) , então será possível visualizar a página disponível em http://localhost/

Para ter acesso a shell do container executando: 

`docker exec -it nome-do-container /bin/bash`

Executa um exemplo a partir de https://github.com/kyriosdata/ig e substitui no apache do container.

Em caso de sucesso o Guia ficará disponível em http://localhost/
