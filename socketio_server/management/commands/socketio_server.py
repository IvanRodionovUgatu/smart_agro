import socketio
from aiohttp import web
from django.core.management import BaseCommand

from project import settings

sio = socketio.AsyncServer(cors_allowed_origins='*')

if settings.DEBUG:
    # https://admin.socket.io для администрирования/дебага сервера
    sio.instrument(
        auth={
            'username': 'admin',
            'password': '',
        }
    )


class Command(BaseCommand):
    args = ''
    help = 'Сервер Socket.io'

    def handle(self, *args: any, **options: any) -> None:
        app = web.Application()
        sio.attach(app)
        web.run_app(app)
