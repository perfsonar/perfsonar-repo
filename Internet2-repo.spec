# $Id$

Summary:    Internet2 Repository file and package configuration
Name:       Internet2-repo
Version:    0.3
Release:    1
License:    distributable, see http://www.internet2.edu/membership/ip.html
Group:      System Environment/Base
URL:        http://software.internet2.edu
Source0:    Internet2-repo.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
Requires:   yum
Requires:   rpm

%description
Internt2 software release file. This package contains yum configuration for the Internet2 RPM Repository, as well as the public GPG keys used to sign them.

%prep
%setup -q -n Internet2-repo

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/etc/yum.repos.d
%{__cp} etc-%{dist}/Internet2.repo $RPM_BUILD_ROOT/etc/yum.repos.d
%{__cp} etc-%{dist}/Internet2-web100_kernel.repo $RPM_BUILD_ROOT/etc/yum.repos.d
%{__mkdir} -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg
%{__cp} etc-%{dist}/RPM-GPG-KEY-Internet2 $RPM_BUILD_ROOT/etc/pki/rpm-gpg

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%if %{!?_without_rpmpubkey:1}0
%pubkey etc/RPM-GPG-KEY-Internet2
%endif
%dir /etc/yum.repos.d/
%config(noreplace) /etc/yum.repos.d
%dir /etc/pki/rpm-gpg/
/etc/pki/rpm-gpg/RPM-GPG-KEY-Internet2

%post
%if %{!?_without_rpmpubkey:1}0
rpm -q gpg-pubkey-9d7b9686-4947b567 &>/dev/null || rpm --import $RPM_BUILD_ROOT/etc/pki/rpm-gpg/RPM-GPG-KEY-Internet2 || :
%endif

%changelog
* Thu Sep 30 2010 Aaron Brown <aaron@internet2.edu> - 0.0.1-3
- Remove apt-rpm support
- Add requirement on yum/rpm
- Add support for web100 kernel repository

* Thu Mar 26 2009 Jason Zurawski <zurawski@internet2.edu> - 0.0.1-2
- Update repo URLs.

* Thu Feb 12 2009 Jason Zurawski <zurawski@internet2.edu> - 0.0.1-1
- Initial package.

