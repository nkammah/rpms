# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%define real_name xclass

Summary: C++ X11 widget set providing win95 look and feel
Name: libxclass
Version: 0.8.2
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://xclass.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/xclass/xclass-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++
%{!?dist:BuildRequires: compat-gcc-c++}
%{?fc3:BuildRequires: compat-gcc-c++}
%{?fc2:BuildRequires: compat-gcc-c++}
%{?fc1:BuildRequires: compat-gcc-c++}
%{?el3:BuildRequires: compat-gcc-c++}
%{?rh9:BuildRequires: compat-gcc-c++}
%{?rh8:BuildRequires: compat-gcc-c++}


Obsoletes: xclass, xclass-devel
Provides: xclass

%description
This widget set allows C++ developers to easily create applications for
the X11 windowing system employing the Windows(tm) 95 look and feel.

These are the header files required by any programmer wishing to author
applications which make use of Xclass and a static library to compile
against.

%prep
%setup -n %{real_name}-%{version}

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|/usr/local/xclass-icons|\@datadir\@/xclass/icons|;
		s|/usr/local/xclass|\@sysconfdir\@/xclass|;
	' lib/libxclass/Makefile.in

%build
%{?fc3:export CXX="g++296"}
%{?fc2:export CXX="g++296"}
%{?fc1:export CXX="g++296"}
%{?el3:export CXX="g++296"}
%{?rh9:export CXX="g++296"}
%{?rh8:export CXX="g++296"}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0644 lib/libxclass/libxclass.a %{buildroot}/%{_libdir}/libxclass.a
%{__install} -D -m0755 config/xc-config %{buildroot}/%{_bindir}/xc-config
%{__install} -D -m0644 doc/xclassrc %{buildroot}/%{_sysconfdir}/xclass/xclassrc

%{__install} -d -m0755 %{buildroot}/%{_includedir}/xclass
%{__install} -m0644 include/xclass/*.h %{buildroot}/%{_includedir}/xclass/

%{__install} -d -m0755 %{buildroot}/%{_datadir}/xclass/icons
%{__install} -m0644 icons/*.xpm %{buildroot}/%{_datadir}/xclass/icons
%{__install} -m0644 lib/libxclass/icons/*.xpm %{buildroot}/%{_datadir}/xclass/icons

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/GPL doc/LGPL doc/LICENSE doc/tcl.license.terms doc/tk.license.terms doc/ChangeLog
%doc doc/INSTALL doc/Layout.notes doc/MimeTypes.README doc/Programming.notes
%config(noreplace) %{_sysconfdir}/xclass/
%{_datadir}/xclass/
%{_bindir}/xc-config
%{_includedir}/xclass/
%{_libdir}/*

%changelog
* Tue Dec 02 2003 Dag Wieers <dag@wieers.com> - 0.8.2-0
- Updated to release 0.8.2.

* Sun Dec 15 2002 Dag Wieers <dag@wieers.com> - 0.7.4-3
- Renamed package "xclass" to packages "libxclass".
- Get rid of useless devel package.

* Sun Dec 15 2002 Dag Wieers <dag@wieers.com> - 0.7.4-0
- Initial package. (using DAR)
