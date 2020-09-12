FROM fedora
#RUN dnf -y install gcc-c++ tar gcc git make rubygem-rake iputils rpmdevtools systemd-rpm-macros -y && dnf clean all
RUN dnf -y install  tar gcc git make rubygem-rake iputils rpmdevtools systemd-rpm-macros -y && dnf clean all

RUN cd && rpmdev-setuptree

COPY Rakefile /root/
COPY packaging/* /root/packaging/
COPY aurora/* /root/aurora/
COPY pvplot/today/* /root/pvplot/today/
COPY shiny-server.conf /root/

RUN cd && rake rpm

