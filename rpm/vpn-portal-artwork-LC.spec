#global git 6ac538130f6d8aab8b0103c5a11df6bca49c2710

Name:       vpn-portal-artwork-LC
Version:    1.1.2
Release:    2%{?dist}
Summary:    VPN Portal Artwork for LC
License:    AGPLv3+

URL:        https://github.com/letsconnectvpn/vpn-portal-artwork
%if %{defined git}
Source0:    https://github.com/letsconnectvpn/vpn-portal-artwork/archive/%{git}/vpn-portal-artwork-%{version}-%{git}.tar.gz
%else
Source0:    https://github.com/letsconnectvpn/vpn-portal-artwork/releases/download/%{version}/vpn-portal-artwork-LC-%{version}.tar.xz
Source1:    https://github.com/letsconnectvpn/vpn-portal-artwork/releases/download/%{version}/vpn-portal-artwork-LC-%{version}.tar.xz.asc
Source2:    gpgkey-6237BAF1418A907DAA98EAA79C5EDD645A571EB2
%endif

BuildArch:  noarch

BuildRequires:  gnupg2

Requires:   vpn-user-portal
Requires:   vpn-admin-portal

%description
VPN Portal Artwork for LC.

%prep
%if %{defined git}
%setup -qn vpn-portal-artwork-%{git}
%else
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -qn vpn-portal-artwork-LC-%{version}
%endif

%install
mkdir -p %{buildroot}%{_datadir}/vpn-user-portal/views/LC
mkdir -p %{buildroot}%{_datadir}/vpn-user-portal/web/css/LC
mkdir -p %{buildroot}%{_datadir}/vpn-user-portal/web/img/LC
mkdir -p %{buildroot}%{_datadir}/vpn-admin-portal/views/LC
mkdir -p %{buildroot}%{_datadir}/vpn-admin-portal/web/css/LC
mkdir -p %{buildroot}%{_datadir}/vpn-admin-portal/web/img/LC

cp -p css/LC.css %{buildroot}%{_datadir}/vpn-user-portal/web/css/LC
cp -p css/LC.css %{buildroot}%{_datadir}/vpn-admin-portal/web/css/LC
cp -p img/LC.png %{buildroot}%{_datadir}/vpn-user-portal/web/img/LC
cp -p img/LC.png %{buildroot}%{_datadir}/vpn-admin-portal/web/img/LC
cp -p views/vpn-user-portal/*.twig %{buildroot}%{_datadir}/vpn-user-portal/views/LC
cp -p views/vpn-admin-portal/*.twig %{buildroot}%{_datadir}/vpn-admin-portal/views/LC

%post
# clear template cache
rm -rf %{_localstatedir}/lib/vpn-user-portal/*/tpl/* >/dev/null 2>/dev/null || :
rm -rf %{_localstatedir}/lib/vpn-admin-portal/*/tpl/* >/dev/null 2>/dev/null || :

%postun
# clear template cache
rm -rf %{_localstatedir}/lib/vpn-user-portal/*/tpl/* >/dev/null 2>/dev/null || :
rm -rf %{_localstatedir}/lib/vpn-admin-portal/*/tpl/* >/dev/null 2>/dev/null || :

%files
%defattr(-,root,root,-)
%{_datadir}/vpn-user-portal/views/LC
%{_datadir}/vpn-user-portal/web/css/LC
%{_datadir}/vpn-user-portal/web/img/LC
%{_datadir}/vpn-admin-portal/views/LC
%{_datadir}/vpn-admin-portal/web/css/LC
%{_datadir}/vpn-admin-portal/web/img/LC
%doc CHANGES.md README.md

%changelog
* Mon Sep 10 2018 François Kooman <fkooman@tuxed.net> - 1.1.2-2
- merge dev and prod spec files in one

* Fri Sep 07 2018 François Kooman <fkooman@tuxed.net> - 1.1.2-1
- update to 1.1.2

* Mon Jul 02 2018 François Kooman <fkooman@tuxed.net> - 1.1.1-2
- use release tarball instead of Git tarball
- verify GPG signature

* Thu May 24 2018 François Kooman <fkooman@tuxed.net> - 1.1.1-1
- update to 1.1.1

* Tue Jan 02 2018 François Kooman <fkooman@tuxed.net> - 1.1.0-2
- artwork moved to own repository

* Tue Dec 05 2017 François Kooman <fkooman@tuxed.net> - 1.1.0-1
- update for template refactor

* Mon Nov 13 2017 François Kooman <fkooman@tuxed.net> - 1.0.0-2
- no longer include README/CHANGES

* Mon Nov 13 2017 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- initial package
