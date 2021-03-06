# $Id$
# Authority: dag
# Upstream: <wireless$kismetwireless,net>

%define _without_gpsmap 1

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: 802.11 (wireless) network sniffer and network dissector
Name: kismet
Version: 3.0.1
%define real_version 2011-01-R1
Release: 201101r1.1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.kismetwireless.net/

Source: http://www.kismetwireless.net/code/kismet-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: byacc
BuildRequires: bzip2-devel
BuildRequires: expat-devel
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: gmp-devel
BuildRequires: ImageMagick-devel
BuildRequires: ncurses-devel
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel
BuildRequires: wget
BuildRequires: zlib-devel
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libX11-devel}

%description
Kismet is an 802.11 (wireless) network sniffer and network dissector.
It is capable of sniffing using most wireless cards, automatic network
IP block detection via UDP, ARP, and DHCP packets, Cisco equipment lists
via Cisco Discovery Protocol, weak cryptographic packet logging, and
Ethereal and tcpdump compatible packet dump files.

%package -n gpsmap
Summary: Tool to plot networks based on kismet files
Group: Applications/Internet

%description -n gpsmap
gpsmap allows to plot networks and estimated network ranges detected by
kismet on downloaded maps or user supplied image files.

%prep
%setup -n %{name}-%{real_version}

### FIXME: Get rid of the ownership changes (RH9)
%{__perl} -pi.orig -e '
        s|-o \$\(INSTUSR\) -g \$\(INSTGRP\) ||g;
        s|-o \$\(INSTUSR\) -g \$\(MANGRP\) ||g;
    ' Makefile.in

### Make dbus.h shut up when dbus < 1.0 (RHEL4 and older)
echo -e "/* make dbus shut up when dbus < 1.0 */\n#define DBUS_API_SUBJECT_TO_CHANGE" >>config.h.in

%build
%configure
#   --enable-syspcap
%{__make} %{?_smp_mflags} dep all

%install
%{__rm} -rf %{buildroot}
%makeinstall rpm \
    ETC="%{buildroot}%{_sysconfdir}" \
    BIN="%{buildroot}%{_bindir}" \
    SHARE="%{buildroot}%{_datadir}/kismet/" \
    MAN="%{buildroot}%{_mandir}" \
    WAV="%{buildroot}%{_datadir}/kismet/wav/"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG GPL README docs/DEVEL.* docs/README*
%doc %{_mandir}/man1/kismet*.1*
%doc %{_mandir}/man5/*.5*
%config(noreplace) %{_sysconfdir}/*
%{_bindir}/kismet*
%{_datadir}/kismet/

%if %{!?_without_gpsmap:1}0
%files -n gpsmap
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/gpsmap.1*
%{_bindir}/gpsmap*
%endif

%changelog
* Wed Jan 26 2011 Dag Wieers <dag@wieers.com> - 3.0.1-201101r1-1
- Updated to release 2011-01-R1.

* Thu Jul 15 2010 Dag Wieers <dag@wieers.com> - 3.0.1-201007r1-1
- Updated to release 2010-07-R1.

* Tue Jan 12 2010 Dag Wieers <dag@wieers.com> - 3.0.1-201001r1-1
- Updated to release 2010-01-R1.

* Sat Dec 26 2009 Dag Wieers <dag@wieers.com> - 3.0.1-200911r1-1
- Updated to release 2009-11-R1.

* Sat Jul 04 2009 Dag Wieers <dag@wieers.com> - 3.0.1-200906r1-1
- Updated to release 2009-06-R1.

* Tue Jun 03 2008 Dag Wieers <dag@wieers.com> - 3.0.1-200805r1-1
- Updated to release 2008-05-R1.

* Mon Oct 08 2007 Dag Wieers <dag@wieers.com> - 3.0.1-200710r1.1
- Updated to release 2007-10-R1.

* Sat Apr 15 2006 Dag Wieers <dag@wieers.com> - 3.0.1-200604r1.1
- Updated to release 2006-04-R1.

* Thu Aug 18 2005 Dag Wieers <dag@wieers.com> - 3.0.1-3.200508r1
- Updated to release 2005-08-R1.

* Mon Jul 25 2005 Dag Wieers <dag@wieers.com> - 3.0.1-2.200507r1
- Updated to release 2005-07-R1.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 3.0.1-2.200506r1
- Updated to release 2005-06-R1.

* Sun Apr 03 2005 Dag Wieers <dag@wieers.com> - 3.0.1-2.200504r1
- Updated to release 2005-04-R1.

* Thu Feb 24 2005 Dag Wieers <dag@wieers.com> - 3.0.1-2.200501r1
- Revert config directory to /etc.
- Updated to release 2005-01-R1.

* Thu Dec 23 2004 Dag Wieers <dag@wieers.com> - 3.0.1-1.200410r1
- Updated to release 2004-10-R1.

* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 3.0.1-1.200404r1
- Updated to release 2004-04-R1.

* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 3.0.1-1
- Updated to release 3.0.1-feb.04.01.

* Wed Aug 13 2003 Dag Wieers <dag@wieers.com> - 3.0.1-0
- Updated to release 3.0.1.

* Thu Jul 31 2003 Dag Wieers <dag@wieers.com> - 3.0.0-0
- Updated to release 3.0.0.

* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 2.8.1-0
- Initial package. (using DAR)
