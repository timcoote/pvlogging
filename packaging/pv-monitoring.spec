Name:       pv-monitoring
Version:    1
Release:    1
Summary:    Monitor and plot pv outputs
License:    FIXME
Requires:   shiny-server
Source0:    https://idontcare.com/pv-monitor.0.0.1.tar.gz

%description
Use curtronic's aurora package to grab data from the PowerONE inverter, stash the data in output, recycle logged data, and
provide plots of data. Initially, these plots are /today, and, day?<date>

%prep
# we have upstream and configuration sources. Need to add. Some of these are better in Rakefile, I think.
%setup

%build
# initially empty
#cat > hello-world.sh <<EOF
#!/usr/bin/bash
#echo Hello world
#EOF

%install
# initially empty
#mkdir -p %{buildroot}/usr/bin/

install -m 755 *R %{buildroot}/srv/shiny-server/examples/today/

%files
/srv/shiny-server/sample-apps/today/ui.R
/srv/shiny-server/sample-apps/today/server.R
/etc/shiny-server/shiny-server.conf

%changelog
# let's skip this for now
