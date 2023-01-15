FROM greycilik/cilikuserbot:buster

RUN git clone -b main https://github.com/CilikProject/Ubot-Telethon /home/Ubot-Telethon/ \
    && chmod 777 /home/ubot-telethon \
    && mkdir /home/ubot-telethon/bin/

COPY ./sample_config.env ./config.env* /home/cilik-ubot/

WORKDIR /home/cilik-ubot/

CMD ["python3", "-m", "CilikUbot"]
