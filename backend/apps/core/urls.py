from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello-world", views.hello_world, name="hello-world"),
    path("debug-task/", views.debug_task_view, name="debug-task",),
    path("celery/sleep-task/", views.sleep_task_view, name="sleep-task"),
    path(
        "debug/send-test-email/",
        views.send_test_email,
        name="send-test-email",
    ),
    path(
        "debug/redis/",
        views.DebugRedis.as_view(
            {"get": "get", "post": "post", "delete": "delete"}
        ),
        name="debug-redis",
    ),
]
