Name:       pv-monitoring
Version:    0.0.2
Release:    1%{?dist}
Summary:    Monitor and plot pv outputs
License:    FIXME
Requires:   shiny-server
Requires:   aurora, strace, logrotate
BuildRequires: systemd-rpm-macros
Source0:    https://idontcare.com/%{name}.%{version}.tar.gz

# See httpd .spec file for systemd integration: https://bit.ly/316IdOB

%description
Use curtronic's aurora package to grab data from the PowerONE inverter, stash the data in output, recycle logged data, and
provide plots of data. Initially, these plots are /today, and, day?<date>

%prep
# we have upstream and configuration sources. Need to add. Some of these are better in Rakefile, I think.
%autosetup

# %%build
# initially empty

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/run/aurora
##make DESTDIR=$RPM_BUILD_ROOT install

install -v -m 755 -D $RPM_BUILD_DIR/pv-monitoring-0.0.2/aurora/run-aurora $RPM_BUILD_ROOT/usr/local/bin/run-aurora 
install -v           $RPM_BUILD_DIR/pv-monitoring-0.0.2/aurora/wrap-aurora $RPM_BUILD_ROOT/usr/local/bin/wrap-aurora 
install -v -m 644 -D $RPM_BUILD_DIR/pv-monitoring-0.0.2/aurora/aurora.logrotate $RPM_BUILD_ROOT/etc/logrotate.d/aurora

# Install systemd service files
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
for s in aurora-logging.service; do
  # ?? install -p -m 644 $RPM_SOURCE_DIR/aurora/${s} \
  # something wrong here. at least need variables
  install -p -m 644 $RPM_BUILD_DIR/pv-monitoring-0.0.2/aurora/${s} \
                    $RPM_BUILD_ROOT%{_unitdir}/${s}
done

#install -m 755 pvplot/today/*R %{buildroot}/srv/shiny-server/examples/today/
ex_dir=srv/shiny-server/sample-apps/today
mkdir -p $RPM_BUILD_ROOT/$ex_dir
install -m 755 pvplot/today/*R $RPM_BUILD_ROOT/$ex_dir
mkdir -p $RPM_BUILD_ROOT/etc/shiny-server
install -m 755 shiny-server.conf $RPM_BUILD_ROOT/etc/shiny-server/

%post
%systemd_post aurora-logging.service

%preun
%systemd_preun aurora-logging.service

%postun
%systemd_postun aurora-logging.service

%files
# %%license add-license-file-here
# %%doc add-docs-here
/srv/shiny-server/sample-apps/today/ui.R
/srv/shiny-server/sample-apps/today/server.R
/etc/shiny-server/shiny-server.conf
%{_unitdir}/aurora-logging.service
/usr/local/bin/run-aurora
/usr/local/bin/wrap-aurora
/var/run/aurora
/etc/logrotate.d/aurora

%changelog
* Sun Aug 16 2020 Tim Coote <tim+github.com@example.com>
- first version
* Sun Sep 6 2020 Tim Coote <tim+github.com@example.com>
- fix app location
