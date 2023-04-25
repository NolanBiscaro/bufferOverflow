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
            apt-get install -y gcc libc6-dev binutils gdb vim emacs

        RUN echo "kernel.randomize_va_space = 0" > /etc/sysctl.d/01-disable-aslr.conf
        '''

        with tempfile.TemporaryDirectory() as tempdir:
            with open(os.path.join(tempdir, "Dockerfile"), "w") as f:
                f.write(dockerfile)

            self.client.images.build(path=tempdir, tag=self.image_name)
    
    def enter_shell_in_sandbox(self, level_vulnerable_code, tempdir):
        # Write the vulnerable code for the current level
        vulnerable_code_path = os.path.join(tempdir, "vulnerable_code.c")
        with open(vulnerable_code_path, "w") as f:
            f.write(level_vulnerable_code)

        # Create an empty file for the user to write their exploit
        exploit_code_path = os.path.join(tempdir, "exploit.py")
        open(exploit_code_path, "w").close()

        # Start the Docker container and drop the user into a shell
        print("Entering the Docker container shell...")
        os.system(f"docker run -it --rm -v {tempdir}:/src {self.image_name} /bin/bash")

        return tempdir

    
    def get_address_information(self, vulnerable_code):
        with tempfile.TemporaryDirectory() as tempdir:
            code_path = os.path.join(tempdir, "vulnerable_code.c")
            with open(code_path, "w") as f:
                f.write(vulnerable_code)

            self.client.containers.run(
                self.image_name,
                volumes={tempdir: {"bind": "/src", "mode": "rw"}},
                command="sh -c 'cd /src && gcc -o vulnerable_code vulnerable_code.c'"
            )

            objdump_output = self.client.containers.run(
                self.image_name,
                volumes={tempdir: {"bind": "/src", "mode": "ro"}},
                command="sh -c 'cd /src && objdump -d -j .text vulnerable_code'"
            )

            objdump_output = objdump_output.decode('utf-8')
            return self.parse_address_information(objdump_output)

    def run_code_in_sandbox(self, code):
        with tempfile.TemporaryDirectory() as tempdir:
            code_path = os.path.join(tempdir, "code.c")
            with open(code_path, "w") as f:
                f.write(code)

            self.client.containers.run(
                self.image_name,
                volumes={tempdir: {"bind": "/src", "mode": "rw"}},
                command="sh -c 'cd /src && gcc -o code code.c && ./code'"
            )

            output = self.client.containers.run(
                self.image_name,
                volumes={tempdir: {"bind": "/src", "mode": "ro"}},
                command="sh -c 'cd /src && ./code'"
            )

        return output.decode("utf-8")

    def run_exploit_against_vulnerable_program(self, tempdir):
        if tempdir:
            #compile the vulnerable.c
            self.client.containers.run(
                self.image_name,
                volumes={tempdir: {"bind": "/src", "mode": "rw"}},
                command="sh -c 'cd /src && gcc -fno-stack-protector -o vulnerable_code vulnerable_code.c'"
            )
            
            output = self.client.containers.run(
                self.image_name,
                volumes={tempdir: {"bind": "/src", "mode": "ro"}},
                command="sh -c 'cd /src && ./vulnerable_code \"$(python3 exploit.py)\"'"
            )

            return output.decode("utf-8")
        return None