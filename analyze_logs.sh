#!/bin/bash

cat <<EOL > access.log
192.168.1.1 - - [28/Jul/2024:12:34:56 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.2 - - [28/Jul/2024:12:35:56 +0000] "POST /login HTTP/1.1" 200 567
192.168.1.3 - - [28/Jul/2024:12:36:56 +0000] "GET /home HTTP/1.1" 404 890
192.168.1.1 - - [28/Jul/2024:12:37:56 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.4 - - [28/Jul/2024:12:38:56 +0000] "GET /about HTTP/1.1" 200 432
192.168.1.2 - - [28/Jul/2024:12:39:56 +0000] "GET /index.html HTTP/1.1" 200 1234
EOL

{
    echo "Отчет анализа логов"

    echo "1. Общее количество запросов:"
    awk 'END {print NR}' access.log
    echo ""

    echo "2. Количество уникальных IP-адресов:"
    awk '{ip[$1]++} END {print length(ip)}' access.log
    echo ""

    echo "3. Количество запросов по методам:"
    awk -F'"' '{print $2}' access.log | awk '{method[$1]++} END {for (m in method) print m ": " method[m]}'
    echo ""

    echo "4. Самый популярный URL:"
    awk -F'"' '{print $2}' access.log | awk '{split($0, a, " "); url[a[2]]++} END {max=0; for (u in url) if (url[u] > max) {max=url[u]; popular=u} print popular ": " max " запросов"}'
} > report.txt

echo "Отчет создан в файле report.txt"