Name:       pv-monitoring
Version:    0.0.7
Release:    3%{?dist}
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
mkdir -p $RPM_BUILD_ROOT/var/log/aurora

# breakage here. Cannot get wrap-aurora to instll with the correct mode
#install -v -m 755 -D $RPM_BUILD_DIR/pv-monitoring-0.0.2/aurora/run-aurora $RPM_BUILD_ROOT/usr/local/bin/run-aurora 
install -v -m 755 -D $RPM_BUILD_DIR/%{name}-%{version}/aurora/run-aurora $RPM_BUILD_ROOT/usr/bin/run-aurora 
install -v           $RPM_BUILD_DIR/%{name}-%{version}/aurora/wrap-aurora $RPM_BUILD_ROOT/usr/bin/wrap-aurora 
install -v -m 644 -D $RPM_BUILD_DIR/%{name}-%{version}/aurora/aurora.logrotate $RPM_BUILD_ROOT/etc/logrotate.d/aurora

# Install systemd service files
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
for s in aurora-logging.service; do
  # ?? install -p -m 644 $RPM_SOURCE_DIR/aurora/${s} \
  # something wrong here. at least need variables
  install -p -m 644 $RPM_BUILD_DIR/%{name}-%{version}/aurora/${s} \
                    $RPM_BUILD_ROOT%{_unitdir}/${s}
done

#install -m 755 pvplot/today/*R %{buildroot}/opt/shiny-server/examples/today/
ex_dir=opt/shiny-server/sample-apps/today
mkdir -p $RPM_BUILD_ROOT/$ex_dir
install -m 755 pvplot/today/*R $RPM_BUILD_ROOT/$ex_dir
mkdir -p $RPM_BUILD_ROOT/etc/shiny-server
install -m 755 shiny-server.conf $RPM_BUILD_ROOT/etc/shiny-server/

%post
%systemd_post aurora-logging.service

%preun
%systemd_preun aurora-logging.service

# fron here: https://bit.ly/3lVmHod, note this for future: https://red.ht/3jTeVcz
%postun
%systemd_postun_with_restart aurora-logging.service

%files
# %%license add-license-file-here
# %%doc add-docs-here
/opt/shiny-server/sample-apps/today/ui.R
/opt/shiny-server/sample-apps/today/server.R
/etc/shiny-server/shiny-server.conf
%{_unitdir}/aurora-logging.service
/usr/bin/run-aurora
/usr/bin/wrap-aurora
/var/log/aurora
/var/run/aurora
/etc/logrotate.d/aurora

%changelog
* Wed Dec 2 2020 Tim Coote <tim+github.com@coote.org>
- fix spellings
- add multiple patches
- move logged data to /var/log/aurora
- bump to 0.0.5

* Sat Sep 12 2020 Tim Coote <tim+github.com@coote.org>
- move from /srv to /opt for rpm-ostree friendliness
- move from /usr/local to /usr for rpm-ostree friendliness

* Mon Sep 7 2020 Tim Coote <tim+github.com@coote.org>
- fix logrotate and systemd integration
- fix timout too low

* Sun Sep 6 2020 Tim Coote <tim+github.com@coote.org>
- fix app location

* Sun Aug 16 2020 Tim Coote <tim+github.com@coote.org>
- first version

