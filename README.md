# API_YAMDB
- [Введение](#введение)
- [Установка](#установка)
- [Загрузка данных](#загрузка-данных)
- [Endpoints](#endpoints)
  - [auth](#auth)
  - [categories](#categories)
  - [genres](#genres)
  - [titles](#titles)
  - [reviews](#reviews)
  - [comments](#comments)
  - [users](#users)
- [О разработчиках](#о-разработчиках)

## Введение
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.
Произведению может быть присвоен жанр (Genre) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

## Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AIBogdanov/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Загрузка данных
В репозитории по пути [/static/data/](/tree/feature/auth/api_yamdb/static/data) находятся примеры csv-файлов c тестовыми данными для используемых баз.
Можно загрузить тестовые данные в проект:
```
python3 manage.py importcsv <base_name> <file_name>
```
Где ```<base_name>``` принимает одно из значений ```user|category|genre|title|review|comment|genretitle```.
Рекомендуемый порядок загрузки данных (некоторые базы могут ссылаться на другие):
```
1. user
2. category
3. genre
4. title
5. review
6. comment
7. genretitle
```

## Endpoints
Для удобства описания и масштабирования протокол, хост и порт приложения опущены, по умолчанию это ```http://localhost:8000```. Все "эндпойнты" приложения начинаются с ```/api/v1```. 
Подробную информацию о них можно посмотреть на странице ```/redoc/```

### auth
Запросы, связанные с регистрацией и авторизацией, начинаются с ```/auth```, принимаются анонимно.
```
/auth/signup/
```
POST-запрос, предназначен для регистрации новых пользователей, входные данные:
```
{
  "email": "string",
  "username": "string"
}
```
При удачном выполнении запроса создаётся пользователь в базе данных и на ```email``` отправляется письмо с кодом подтверждения.

```
/auth/token/
```
POST-запрос, предназначен для получения JWT-токена, который будет использоваться при последующей авторизации, входные данные:
```
{
"username": "string",
"confirmation_code": "string"
}
```
При удачном выполнении запроса выдаётся ответ в формате:
```
{
"token": "string"
}
```

### categories
Запросы, связанные с категориями произведений, начинаются с ```/categories```
```
/categories/
```
GET-запрос выдаёт список всех категорий, воспользоваться может даже анонимный пользователь. В случае POST-запроса требуется доступ администратора и принимаются следующие входные данные:
```
{
  "name": "string",
  "slug": "string"
}
```
При успешном выполнении создаётся новая категория с соответствующими именем и slug-путём.
```
/categories/{slug}/
```
DELETE-запрос, который удаляет категорию с соответствующим slug-путём. Требуется доступ администратора.

### genres
Запросы, связанные с жанрами произведений, начинаются с ```/genres```
```
/genres/
```
GET-запрос выдаёт список всех жанров, воспользоваться может даже анонимный пользователь. В случае POST-запроса требуется доступ администратора и принимаются следующие входные данные:
```
{
  "name": "string",
  "slug": "string"
}
```
При успешном выполнении создаётся новый жанр с соответствующими именем и slug-путём.
```
/genres/{slug}/
```
DELETE-запрос, который удаляет жанр с соответствующим slug-путём. Требуется доступ администратора.

### titles
Запросы, связанные непосредственно с произведениями, начинаются с ```/titles```
```
/titles/
```
GET-запрос выдаёт список всех произведений, воспользоваться может даже анонимный пользователь. В случае POST-запроса требуется доступ администратора и принимаются следующие входные данные:
```
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```
При успешном выполнении создаётся новое произведение с соответствующими данными.
```
/titles/{titles_id}/
```
GET-запрос выдаёт подробную информацию о произведении, воспользоваться может даже анонимный пользователь. В случае PATCH-запроса требуется доступ администратора и принимаются те же входные данные, что и для POST-запроса ```/titles/```, DELETE-запрос - требует администраторских прав и удаляет произведение с соответствующим id.

### reviews
Запросы, связанные с отзывами на произведения, начинаются с ```/titles/{title_id}/reviews```
```
/titles/{title_id}/reviews/
```
GET-запрос выдаёт список всех произведений, воспользоваться может даже анонимный пользователь. В случае POST-запроса требуется доступ уровня пользователя (и выше) и принимаются следующие входные данные:
```
{
  "text": "string",
  "score": int(1..10)
}
```
При успешном выполнении создаётся новый отзыв с соответствующими данными.
```
{
  "id": int,
  "text": "string",
  "author": "string",
  "score": int(1..10),
  "pub_date": "YYYY-MM-DDTHH:MM:SS"
}
```
где поля ```id, author, pub_date``` заполняются автоматически.

```
/titles/{title_id}/reviews/{review_id}/
```
GET-запрос выдаёт подробную информацию о произведении, воспользоваться может даже анонимный пользователь. В случае PATCH-запроса требуется быть автором отзыва или иметь уровень модератора и выше и принимаются те же входные данные, что и для POST-запроса ```/titles/{title_id}/reviews/```, DELETE-запрос - требует тех же прав, что и PATCH, и удаляет отзыв с соответствующим id.

### comments
Запросы, связанные с комментариями на отзывы на произведения, начинаются с ```/titles/{title_id}/reviews/{review_id}/comments```
```
/titles/{title_id}/reviews/{review_id}/comments/
```
GET-запрос выдаёт список всех комментариев к отзыву, воспользоваться может даже анонимный пользователь. В случае POST-запроса требуется доступ уровня пользователя (и выше) и принимаются следующие входные данные:
```
{
  "text": "string"
}
```
При успешном выполнении создаётся новый отзыв с соответствующими данными.
```
{
  "id": int,
  "text": "string",
  "author": "string",
  "pub_date": "YYYY-MM-DDTHH:MM:SS"
}
```
где поля ```id, author, pub_date``` заполняются автоматически.

```
/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
GET-запрос выдаёт подробную информацию о произведении, воспользоваться может даже анонимный пользователь. В случае PATCH-запроса требуется быть автором отзыва или иметь уровень модератора и выше и принимаются те же входные данные, что и для POST-запроса ```/titles/{title_id}/reviews/{review_id}/comments/```, DELETE-запрос - требует тех же прав, что и PATCH и удаляет комментарий с соответствующим id.

### users
Запросы, связанные с управлением пользователями, начинаются с ```/users```
```
/users/
```
GET-запрос выдаёт список всех пользователей, воспользоваться может только администратор. В случае POST-запроса требуется доступ уровня администратора и принимаются следующие входные данные:
```
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user|moderator|administrator"
}
```
При успешном выполнении создаётся новый пользователь с соответствующими данными.
```
/users/{username}/
```
Все запросы к этому эндпойтну требуют уровнь администратора, ```username``` не может быть ```me```. GET-запрос выдает подробную информацию о пользователе. В случае PATCH-запроса принимаются те же входные данные, что и для POST-запроса ```/users/```, DELETE-запрос - удаляет соответствующего пользователя.
```
/users/me/
```
Эндпойнт для работы с текущим (под которым авторизован) пользователем. GET-запрос выдаёт подробную информацию о пользователе, а PATCH-запрос позволяет её отредактировать, применяются те же входные данные, что и для PATCH-запроса ```/users/{username}/```

# О разработчиках
Над проектом трудились 3 разработчика:
- [Байрамов Денис](https://github.com/Vilenor/)
- [Богданов Андрей](https://github.com/AIBogdanov/)
- [Боровков Николай](https://github.com/NnExe/)

Денис занимался разработкой [категорий](#categories), [жанров](#genres) и [произведений](#titles). Андрей был тимлидом команды и занимался разработкой [отзывов](#reviews) и [комментариев](#comments). Николай занимался [авторизацией](#auth), [пользователями](#users) и [скриптом загрузки данных](#загрузка-данных).