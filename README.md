<h1>BMSTU Passport Control System</h1>
<h3>Умное управление паспортами и пересечениями границы</h3>

<p>Приложение для хранения данных о паспортах, подачи заявок на пересечение границы и работы с сопутствующими данными — всё это в красивом и удобном интерфейсе!</p>

<hr>

<h2>Возможности</h2>
<ul>
  <li><strong>Загрузка паспортов</strong> с фотографией (MinIO)</li>
  <li><strong>Поиск, фильтрация</strong> и просмотр паспортов</li>
  <li><strong>Формирование заявок</strong> с множеством услуг</li>
  <li><strong>Редактирование заявок</strong> в статусе черновика</li>
  <li><strong>Составной уникальный ключ</strong> между заявкой и паспортами</li>
  <li><strong>Удаление заявок</strong> через SQL (мягкое удаление)</li>
  <li><strong>Поддержка прав доступа</strong>: пользователь, модератор</li>
  <li><strong>Swagger-документация</strong> с авторизацией</li>
  <li><strong>Тестирование</strong> через Postman / Insomnia</li>
  <li><strong>SPA-интерфейс</strong> на React + Redux Toolkit</li>
  <li><strong>Адаптивный интерфейс</strong> + мобильная PWA</li>
  <li><strong>Нативное приложение</strong> через Tauri</li>
</ul>

<hr>

<h2>Технологии</h2>
<ul>
  <li>Python 3.10 + Django</li>
  <li>PostgreSQL + Docker</li>
  <li>MinIO для хранения изображений</li>
  <li>React, TypeScript, Redux Toolkit</li>
  <li>Swagger + JWT / session-based auth</li>
  <li>Redis (сессии)</li>
  <li>Tauri (кроссплатформенный клиент)</li>
  <li>GitHub Pages + PWA</li>
</ul>

<hr>

<h2>Как запустить</h2>
<ol>
  <li>Клонируй репозиторий:
    <pre><code>git clone https://github.com/yourname/border-passport-app.git
cd border-passport-app</code></pre>
  </li>
  <li>Подними PostgreSQL в Docker:
    <pre><code>docker run --name pg-docker \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=mydatabase \
  -p 5432:5432 \
  -d postgres</code></pre>
  </li>
  <li>Создай .env или пропиши данные в settings.py</li>
  <li>Применяй миграции и запускай:
    <pre><code>python manage.py makemigrations
python manage.py migrate
python manage.py runserver</code></pre>
  </li>
</ol>

<hr>

<h2>Планы на будущее</h2>
<ul>
  <li>Разработка полноценного REST API с бизнес-логикой заявок</li>
  <li>Формирование и завершение заявок с расчетом стоимости</li>
  <li>Разграничение прав доступа (автор, модератор, гость)</li>
  <li>Swagger UI с интерактивной авторизацией</li>
  <li>JWT и сессионная авторизация, проверка прав доступа</li>
  <li>Интеграция с Redis для хранения сессий</li>
  <li>Интерфейс SPA на React с фильтрами, breadcrumbs, загрузкой картинок</li>
  <li>Поддержка PWA, мобильной версии и адаптивной верстки</li>
  <li>Создание Tauri-приложения с подключением по IP</li>
  <li>Redux Toolkit для хранения фильтров и состояния заявок</li>
  <li>Генерация кода клиента через Swagger (axios, redux-thunk)</li>
  <li>Разработка диаграмм (class, sequence, activity, deployment)</li>
</ul>

<hr>

<h2>Авторство</h2>
<p>
<strong>Автор:</strong> Alexandr Shcherbakov<br>
<strong>Дата:</strong> апрель 2025<br>
<strong>Поддержка:</strong> <a href="https://t.me/angel_roto">@angel_roto</a>
</p>
