from django.core.management import call_command
from threading import Thread

class RunCommandOnServerStartMiddleware:
    _command_executed = False

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not RunCommandOnServerStartMiddleware._command_executed:
            RunCommandOnServerStartMiddleware._command_executed = True
            Thread(target=self.run_command).start()
        return self.get_response(request)

    def run_command(self):
        call_command('create_superuser_if_not_exists')