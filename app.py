from asgi_tortoise_orm.middleware import TortoiseMiddleware

from myapp.models import MyModel


class App:
    def __init__(self, scope):
        self.scope = scope

    async def __call__(self, recieve, send):
        my_model = MyModel(name="My test")
        await my_model.save()

        my_model_obj = await MyModel.first()
        content = f"id={my_model_obj.id} name={my_model_obj.name}"

        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [[b"content-type", b"text/html; charset=utf-8"]],
            }
        )
        await send(
            {"type": "http.response.body", "body": content.encode(), "more_body": False}
        )


app = TortoiseMiddleware(App)
