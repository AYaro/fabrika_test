# Fabrika Test Task


Как запустить?

```sh
$ cd fabrika_test
$ docker build -t test_task .
$ docker run -p 8000:8000 test_task  
```
Документвция после запуска будет доступна тут:
 http://localhost:8000/api/redoc/api/redoc
 
Пример работы?

  - /api/token/obtain/ - получение токена

    по умолчанию username админа - admin

    пароль - password1234

    пример: 
    ```
        curl --request POST \
      --url http://localhost:8000/api/token/obtain/ \
      --header 'content-type: application/json' \
      --data '
    {
    	"username":"admin",
    	"password":"password1234"
    }'
    ```
    полученный (access) токен кладем в загалоки запроса 
  - /api/core/apps/ - Создание Приложепния: 
  
      ```
      curl --request POST \
      --url http://localhost:8000/api/core/apps/ \
      --header 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg5MzA5OTMzLCJqdGkiOiI4YmU5MmM5NmMyYWE0ZGE2YjQzMjIyOGI3MTA2NTc3ZSIsInVzZXJfaWQiOjF9.2vElBATKxDTx9xvXTdekCLzdT50BHvvmwyQffaygyYY' \
      --header 'content-type: application/json' \
      --data '{
    	"name":"A test app",
    	"api":"some test api key"
    }'
      ```
- по api/core/apps/test/ можно получить приложение передав ключ
- по api/core/apps/ - cписок приложений, если ты админ то все, включая удаленные, если не админ, то только не удаленные
  


