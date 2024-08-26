### Systemd timers

ref: https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html

- unit files ending with the `.timer` suffix that allow to execute a service based on time.
- can be used as an alternative to cron.
- listing all systemd timers

    $ systemctl list-timers
