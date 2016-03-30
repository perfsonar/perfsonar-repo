# $Id$

Summary:    Internet2 Repository file and package configuration
Name:       Internet2-repo
Version:    0.7
Release:    1 
License:    distributable, see http://www.internet2.edu/membership/ip.html
Group:      System Environment/Base
URL:        http://software.internet2.edu
Source0:    Internet2-repo.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
Requires:   yum
Requires:   rpm
Obsoletes:  Internet2-epel6-repo <= 0.1-1

%description
Internt2 software release file. This package contains yum configuration for the Internet2 RPM Repository, as well as the public GPG keys used to sign them.

%package nightly
Summary:    Internet2 nightly repository
Group:      System Environment/Base
Requires:   Internet2-repo

%description nightly
Configures yum to use Internet2 nightly repository

%package staging
Summary:    Internet2 staging repository
Group:      System Environment/Base
Requires:   Internet2-repo

%description staging
Configures yum to use Internet2 staging repository

%prep
%setup -q -n Internet2-repo

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/etc/yum.repos.d
%{__cp} etc%{dist}/Internet2.repo $RPM_BUILD_ROOT/etc/yum.repos.d
%{__cp} etc%{dist}/Internet2-web100_kernel.repo $RPM_BUILD_ROOT/etc/yum.repos.d
%{__cp} etc%{dist}/Internet2-Vault.repo $RPM_BUILD_ROOT/etc/yum.repos.d
%{__cp} etc%{dist}/Internet2-nightly.repo $RPM_BUILD_ROOT/etc/yum.repos.d
%{__cp} etc%{dist}/Internet2-staging.repo $RPM_BUILD_ROOT/etc/yum.repos.d
%{__mkdir} -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg
%{__cp} etc%{dist}/RPM-GPG-KEY-Internet2 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
%{__cp} etc%{dist}/RPM-GPG-KEY-Internet2-testing $RPM_BUILD_ROOT/etc/pki/rpm-gpg

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%if %{!?_without_rpmpubkey:1}0
%pubkey etc%{dist}/RPM-GPG-KEY-Internet2
%endif
%config(noreplace) /etc/yum.repos.d/Internet2.repo
%config(noreplace) /etc/yum.repos.d/Internet2-web100_kernel.repo
%config(noreplace) /etc/yum.repos.d/Internet2-Vault.repo
%dir /etc/pki/rpm-gpg/
/etc/pki/rpm-gpg/RPM-GPG-KEY-Internet2
/etc/pki/rpm-gpg/RPM-GPG-KEY-Internet2-testing

%files nightly
%defattr(-, root, root, 0755)
%config(noreplace) /etc/yum.repos.d/Internet2-nightly.repo

%files staging
%defattr(-, root, root, 0755)
%config(noreplace) /etc/yum.repos.d/Internet2-staging.repo

%post
%if %{!?_without_rpmpubkey:1}0
rpm -q gpg-pubkey-9d7b9686-4947b567 &>/dev/null || rpm --import $RPM_BUILD_ROOT/etc/pki/rpm-gpg/RPM-GPG-KEY-Internet2 || :
rpm -q gpg-pubkey-242b3ccc-55816f7b &>/dev/null || rpm --import $RPM_BUILD_ROOT/etc/pki/rpm-gpg/RPM-GPG-KEY-Internet2-testing || :
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

