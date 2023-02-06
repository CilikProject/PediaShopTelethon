FROM greycilik/cilikuserbot:buster

RUN git clone -b main https://github.com/CilikProject/Near-Ubot-Telethon-DelaySpam /home/near-ubot-telethon-delayspam/ \
    && chmod 777 /home/near-ubot-telethon-delayspam \
    && mkdir /home/near-ubot-telethon-delayspam/bin/

COPY ./sample_config.env ./config.env* /home/near-ubot-telethon-delayspam/

WORKDIR /home/near-ubot-telethon-delayspam/

CMD ["python3", "-m", "CilikUbot"]
