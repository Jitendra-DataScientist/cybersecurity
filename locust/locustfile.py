from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Simulate user waiting between requests

    @task
    def home_page(self):
        self.client.get("/")  # Replace with specific paths if needed
