Name:       pv-monitoring
Version:    0.0.1
Release:    1%{?dist}
Summary:    Monitor and plot pv outputs
License:    FIXME
Requires:   shiny-server
Requires:   aurora
Source0:    https://idontcare.com/%{name}.%{version}.tar.gz

%description
Use curtronic's aurora package to grab data from the PowerONE inverter, stash the data in output, recycle logged data, and
provide plots of data. Initially, these plots are /today, and, day?<date>

%prep
# we have upstream and configuration sources. Need to add. Some of these are better in Rakefile, I think.
%autosetup

# %%build
# initially empty
#cat > hello-world.sh <<EOF
#!/usr/bin/bash
#echo Hello world
#EOF

%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT/var/run/aurora
# %%make_install

#install -m 755 pvplot/today/*R %{buildroot}/srv/shiny-server/examples/today/
ex_dir=srv/shiny-server/sample-apps/today
mkdir -p $RPM_BUILD_ROOT/$ex_dir
install -m 755 pvplot/today/*R $RPM_BUILD_ROOT/$ex_dir
mkdir -p $RPM_BUILD_ROOT/etc/shiny-server
install -m 755 shiny-server.conf $RPM_BUILD_ROOT/etc/shiny-server/

%files
# %%license add-license-file-here
# %%doc add-docs-here
/srv/shiny-server/sample-apps/today/ui.R
/srv/shiny-server/sample-apps/today/server.R
/etc/shiny-server/shiny-server.conf

%changelog
* Sun Aug 16 2020 Tim Coote <tim+github.com@example.com>
- first version
