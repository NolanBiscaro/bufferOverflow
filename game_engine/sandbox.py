import docker
import os
import tempfile

class Sandbox:
    def __init__(self):
        self.client = docker.from_env()
        self.image_name = "sandbox_image"

        self.prepare_sandbox_image()

    def prepare_sandbox_image(self):
        dockerfile = '''
        FROM ubuntu:latest

        RUN apt-get update && \
            apt-get install -y gcc libc6-dev
        '''

        with tempfile.TemporaryDirectory() as tempdir:
            with open(os.path.join(tempdir, "Dockerfile"), "w") as f:
                f.write(dockerfile)

            self.client.images.build(path=tempdir, tag=self.image_name)

    def run_level_code(self, level_code):
        return self.run_code_in_sandbox(level_code)

    def run_exploit_code(self, exploit_code):
        return self.run_code_in_sandbox(exploit_code)

    def run_code_in_sandbox(self, code):
        with tempfile.TemporaryDirectory() as tempdir:
            code_path = os.path.join(tempdir, "code.c")
            with open(code_path, "w") as f:
                f.write(code)

            self.client.containers.run(
                self.image_name,
                volumes={tempdir: {"bind": "/src", "mode": "ro"}},
                command="sh -c 'cd /src && gcc -o code code.c && ./code'"
            )

            output = self.client.containers.run(
                self.image_name,
                volumes={tempdir: {"bind": "/src", "mode": "ro"}},
                command="sh -c 'cd /src && ./code'"
            )

        return output.decode("utf-8")