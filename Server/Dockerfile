FROM ubuntu

RUN apt-get -qq update && apt-get -qq install -y --no-install-recommends \
    openssh-server \
  && apt-get -qq clean \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/run/sshd \
  && mkdir /root/.ssh \
  && chmod 700 /root/.ssh \
  && touch /root/.ssh/authorized_keys \
  && echo "root:root" | chpasswd 

COPY bin/* /usr/local/bin/
COPY sshd_config /etc/ssh/sshd_config

EXPOSE 22

ENTRYPOINT ["ssh-start"]
CMD ["ssh-server"]

COPY authorized_keys /root/.ssh/authorized_keys
