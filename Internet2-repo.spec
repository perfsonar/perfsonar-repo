# $Id$

Summary:    Internet2 Repository file and package configuration
Name:       Internet2-repo
Version:    0.1
Release:    2
License:    distributable, see http://www.internet2.edu/membership/ip.html
Group:      System Environment/Base
URL:        http://software.internet2.edu
Source0:    Internet2-repo.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

%description
Internt2 software release file. This package contains apt and yum configuration for the Internet2 RPM Repository, as well as the public GPG keys used to sign them.

%prep
%setup -q -n Internet2-repo

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/etc/apt/sources.list.d
%{__cp} etc/Internet2.list $RPM_BUILD_ROOT/etc/apt/sources.list.d
%{__mkdir} -p $RPM_BUILD_ROOT/etc/yum.repos.d
%{__cp} etc/Internet2.repo $RPM_BUILD_ROOT/etc/yum.repos.d
%{__cp} etc/mirrors-Internet2 $RPM_BUILD_ROOT/etc/yum.repos.d
%{__mkdir} -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg
%{__cp} etc/RPM-GPG-KEY-Internet2 $RPM_BUILD_ROOT/etc/pki/rpm-gpg

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%if %{!?_without_rpmpubkey:1}0
%pubkey etc/RPM-GPG-KEY-Internet2
%endif
%dir /etc/apt/
%dir /etc/apt/sources.list.d/
%config(noreplace) /etc/apt/sources.list.d/Internet2.list
%dir /etc/yum.repos.d/
%config(noreplace) /etc/yum.repos.d/Internet2.repo
%config /etc/yum.repos.d/mirrors-Internet2
%dir /etc/pki/rpm-gpg/
/etc/pki/rpm-gpg/RPM-GPG-KEY-Internet2

%post
%if %{!?_without_rpmpubkey:1}0
rpm -q gpg-pubkey-9d7b9686-4947b567 &>/dev/null || rpm --import $RPM_BUILD_ROOT/etc/pki/rpm-gpg/RPM-GPG-KEY-Internet2 || :
%endif

%changelog
* Thu Mar 26 2009 Jason Zurawski <zurawski@internet2.edu> - 0.0.1-2
- Update repo URLs.

* Thu Feb 12 2009 Jason Zurawski <zurawski@internet2.edu> - 0.0.1-1
- Initial package.

