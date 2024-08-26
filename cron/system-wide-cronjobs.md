- `/etc/crontab` and `/etc/cron.d/*` are system-wide crontab files editable only by a system administrator
- listing system-wide cron jobs

    $ cat /etc/crontab /etc/cron.d/*

- in most linux distributions, it's possible to also put an *executable* script inside `/etc/cron.{hourly,daily,weekly,monthly}` and they'll execute accordingly.
