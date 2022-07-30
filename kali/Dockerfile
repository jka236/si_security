FROM kalilinux/kali-rolling

# Run basic commands to update the image
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt dist-upgrade -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold"
RUN apt autoremove -y
RUN apt clean -y
RUN apt install kali-linux-headless -yqq -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold"