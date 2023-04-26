FROM i386/ubuntu:18.04

        RUN apt-get update && \
            apt-get install -y gcc libc6-dev binutils gdb vim emacs

        RUN echo "kernel.randomize_va_space = 0" > /etc/sysctl.d/01-disable-aslr.conf
