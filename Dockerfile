FROM greycilik/cilikuserbot:buster

RUN git clone -b main https://github.com/CilikProject/Ubot-Telethon /home/ubot-telethon/ \
    && chmod 777 /home/ubot-telethon \
    && mkdir /home/ubot-telethon/bin/

COPY ./sample_config.env ./config.env* /home/ubot-telethon/

WORKDIR /home/ubot-telethon/

CMD ["python3", "-m", "CilikUbot"]
