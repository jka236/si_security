# si_security

# Commands

If it is your first time to run, use `./manage.sh build` command.
<br>If you have built the image before, use `./manage.sh up` to start.
<br>After the lab, kill the kali shell by entering `exit` and typing `./manage.sb stop` on your local machine to stop containers

>./manage.sh build
>- Build DVWA image with netcat and vim installation (Other packages can be added if necessary).
>- Build Kali-linux image with a Kali-Linux-headless package
>- Start DWVA container and run an interactive Kali linux shell
>- Localhost port 80 combined with DWVA

>./manage.sh up
>- Start DVWA container
>- Start and attach Kali linux container which starts an interactive shell
>- Localhost port 80 combined with DWVA

>./manage.sh stop
>- Stop DVWA & Kali Liux containers

***Error handling is needed to be implemented***
