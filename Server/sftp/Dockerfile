FROM ubuntu

RUN apt-get -qq update && apt-get -qq install -y --no-install-recommends \
    openssh-server sudo \
  && apt-get -qq clean \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/run/sshd \
  && mkdir /root/.ssh \
  && chmod 700 /root/.ssh \
  && touch /root/.ssh/authorized_keys \
  && useradd matthias -m -d /home/matthias -g sudo -p fxE22Fbm9eV1g \
  && yes | unminimize 


COPY bin/* /usr/local/bin/
COPY sshd_config /etc/ssh/sshd_config

# Chrooted sftp
RUN groupadd sftponly \
  &&  useradd -p "sCBMjyQNUeegc" -g sftponly -m -d /home/sftp sftp \
  &&  chown root:root /home/sftp \
  &&  chmod 0755 /home/sftp \
  &&  mkdir /home/sftp/files \
  &&  chown sftp /home/sftp/files

EXPOSE 22

ENTRYPOINT ["ssh-start"]
CMD ["ssh-server"]

COPY authorized_keys /root/.ssh/authorized_keys
