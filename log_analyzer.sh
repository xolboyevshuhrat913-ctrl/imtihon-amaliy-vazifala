#!/bin/bash


LOG_FILE="$1"

if [ -z "$LOG_FILE" ]; then
    echo "Foydalanish: $0 <log_fayl>"
    exit 1
fi


if [ ! -f "$LOG_FILE" ]; then
    echo "Xatolik: '$LOG_FILE' fayli topilmadi!"
    exit 1
fi


TOTAL=$(wc -l < "$LOG_FILE")


ERRORS=$(grep "ERROR" "$LOG_FILE" | wc -l)


WARNINGS=$(grep "WARNING" "$LOG_FILE" | wc -l)


echo "==================================="
echo "        LOG TAHLIL HISOBOTI"
echo "==================================="
echo "Fayl              : $LOG_FILE"
echo "Umumiy qatorlar   : $TOTAL"
echo "ERROR qatorlar    : $ERRORS"
echo "WARNING qatorlar  : $WARNINGS"
echo "==================================="
