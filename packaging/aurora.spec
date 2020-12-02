Name:       aurora
Version:    1.9.3
Release:    3%{?dist}
Summary:    Log data from Aurora inverter
License:    FIXME
Source0:    http://www.curtronics.com/Solar/ftp/aurora-1.9.3.tar.gz
Patch0:      aurora.patch
Patch1:      aurora-unlocal.patch

%description
Logs data from the Aurora Power One inverter.

%prep
# we have upstream and configuration sources. Need to add. Some of these are better in Rakefile, I think.
%autosetup

%build
%make_build ARCH=NONE TUNE=generic

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
# %%license add-license-file-here
# %%doc add-docs-here
/usr/bin/aurora
%doc /usr/share/man/man1/aurora.1.gz

%changelog
* Sat Sep 12 2020 Tim Coote <tim+github.com@coote.org>
- move from /usr/local to /usr

* Mon Aug 17 2020 Tim Coote <tim+github.com@coote.org>
- rpm of released code
* Sun Sep 6 2020 Tim Coote <tim+github.com@coote.org>
- generic compilation to avoid Illegal Instruction
