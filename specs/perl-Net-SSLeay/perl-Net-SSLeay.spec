# $Id$
# Authority: dag

%define real_name Net_SSLeay.pm

Summary: Net-SSLeay module for perl
Name: perl-Net-SSLeay
Version: 1.25
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SSLeay.pm/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/S/SA/SAMPO/Net_SSLeay.pm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Net-SSLeay module for perl.

%prep
%setup -n %{real_name}-%{version} 

%{__perl} -pi -e 's|^\s*#!/.*bin/perl|#!%{__perl}|;' SSLeay.pm examples/*.pl

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL %{_prefix} \
        PREFIX="%{buildroot}%{_prefix}" \
        INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} config static dynamic \
        OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes Credits MANIFEST QuickRef README examples/*
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*/Net/
%{_libdir}/perl5/vendor_perl/*/*/auto/Net/

%changelog
* Fri Nov 12 2004 Dries Verachtert <dries@ulyssis.org> 1.25-1
- Workaround directory-conflicts bug in up2date. (RHbz #106123)

* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> 1.25-0
- Update to release 1.25.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 1.23-0
- Initial package. (using DAR)
