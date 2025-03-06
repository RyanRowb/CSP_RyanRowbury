    time_t now = time(NULL);
    struct tm *tm_truckt = localtime(&now);
    int hour = tm_truckt->tm_hour;
    scanf("%d", hour);