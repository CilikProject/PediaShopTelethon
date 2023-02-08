FROM greycilik/cilikuserbot:buster

RUN git clone -b main https://github.com/CilikProject/PediaShopTelethon /home/pediashoptelethon/ \
    && chmod 777 /home/pediashoptelethon \
    && mkdir /home/pediashoptelethon/bin/

COPY ./sample_config.env ./config.env* /home/pediashoptelethon/

WORKDIR /home/pediashoptelethon/

CMD ["python3", "-m", "CilikUbot"]
