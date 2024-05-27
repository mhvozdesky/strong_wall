# Strong Wall Project

## Project Description
The Strong Wall project demonstrates basic protection against DDoS attacks. It is presented as a simple greeting web application. The frontend is implemented in React.js, and the backend in Django.

On the main page, the user can enter their name and be greeted. After clicking the "Greet" button, a request is sent to the backend. If the entered name is already in the database, the user will see a message indicating they have already met, otherwise, it will display "Hello, [name]". This is a simple implementation to illustrate some action on a web page.

## Using Google reCAPTCHA
One of the verification steps is Google reCAPTCHA, which ensures that the request is sent by a human and not an automated bot.

## Rate Limiting
The main check for unwanted activity is implemented on the backend in the `RateLimitMiddleware`. The project settings specify that no more than 5 requests can be sent within 60 seconds.

When a request comes in, we get the user's IP address and record it in the cache (Redis) with a timestamp. Each time we check how many requests have been made in the last 60 seconds. If more than 5 requests have been made, this IP address is blocked for 10 minutes.

### Step-by-Step Verification Description
1. Obtain the IP address.
2. Check if the IP address is blocked. If blocked, send a 403 status with an explanation that the IP is temporarily blocked.
3. Check if the request limit is exceeded. If more than 5 requests have been made from this IP address in the last 60 seconds, send a 429 status with the explanation "Too many requests".
4. If all checks are passed, process the request.

### Checking if the Limit is Exceeded
1. Obtain the timestamp.
2. Form a `cache_key` for recording in Redis.
3. Retrieve the list of timestamps for this IP address from the cache for the last 60 seconds.
4. Add the new timestamp from the current request to the retrieved list.
5. If the number of timestamps exceeds the limit, the check is not passed.

Using middleware allows checking all requests within the entire web application, not just a specific endpoint.

## Production Recommendations
To combat DDoS attacks in production, we can add a load balancer with automatic scaling (typical for cloud infrastructures). We can also add a WAF in Nginx or Apache. When the web application is deployed in production, third-party services can be used.

## Requirements
- Node.js 18
- Python 3.10
- Redis 6
- Postgres 15
- Django 5

## Using Google reCAPTCHA
The project uses Google reCAPTCHA. You need to have a `site key` and a `secret key`.

## Starting the Frontend
1. Navigate to the `strong_wall_frontend` directory with the command:
    ```sh
    cd strong_wall_frontend
    ```

2. Install the dependencies:
    ```sh
    npm install
    npm install http-proxy-middleware --save
    npm install react-google-recaptcha
    ```

3. Start the development server:
    ```sh
    npm start
    ```

    **Attention!** In the `src/components/Greeting.jsx` file, you need to replace the `sitekey` with your own, obtained from the Google reCAPTCHA settings.

## Starting the Backend
1. From the project root, navigate to the `strong_wall_backend` directory:
    ```sh
    cd strong_wall_backend
    ```

    **Recommendation:** Use a virtual environment.

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run migrations (you need to have the database and Redis running):
    ```sh
    python manage.py migrate
    ```

4. Start the development server:
    ```sh
    python manage.py runserver
    ```

## Backend Configuration
To work with the backend, you need to have a file with environment variables. Here is an example `.env` file:

```env
DJANGO_SECRET_KEY=<your_django_secret_key>
DJANGO_DEBUG=1
STRONG_WALL_ALLOWED_HOSTS=<your_allowed_hosts>
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<your_db_name>
DB_USER=<your_db_user>
DB_PASSWORD=<your_db_password>
DB_HOST=<your_db_host>
DB_PORT=<your_db_port>
REDIS_HOST=<your_redis_host>
REDIS_PORT=<your_redis_port>
POSTGRES_USER=<your_postgres_user>
POSTGRES_PASSWORD=<your_postgres_password>
POSTGRES_DB=<your_postgres_db>
RECAPTCHA_SECRET_KEY=<your_recaptcha_secret_key>
