from tortoise import Tortoise

from myapp.models import MyModel


class TortoiseMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, scope):
        return _TortoiseResponder(self.app, scope)


class _TortoiseResponder:
    def __init__(self, app, scope):
        self.app = app
        self.scope = scope

    async def __call__(self, receive, send):
        await Tortoise.init(
            db_url="postgres://localhost:5432/tortoise",
            modules={"models": ["myapp.models"]},
        )
        asgi = self.app(self.scope)
        await asgi(receive, send)


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
