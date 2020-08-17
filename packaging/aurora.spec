Name:       aurora
Version:    1.9.3
Release:    1%{?dist}
Summary:    Log data from Aurora inverter
License:    FIXME
Requires:   shiny-server
Source0:    http://www.curtronics.com/Solar/ftp/aurora-1.9.3.tar.gz
Patch:      aurora.patch

%description
Logs data from the Aurora Power One inverter.

%prep
# we have upstream and configuration sources. Need to add. Some of these are better in Rakefile, I think.
%autosetup

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
# %%license add-license-file-here
# %%doc add-docs-here
/usr/local/bin/aurora
%doc /usr/local/share/man/man1/aurora.1

%changelog
* Mon Aug 17 2020 Tim Coote <tim+github.com@example.com>
- rpm of released code
