from tortoise import Tortoise


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
