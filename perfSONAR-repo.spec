# $Id$

Summary:    perfSONAR Repository file and package configuration
Name:       perfSONAR-repo
Version:    0.10
Release:    1
License:    distributable, see http://www.internet2.edu/membership/ip.html
Group:      System Environment/Base
URL:        http://software.internet2.edu
Source0:    perfSONAR-repo.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
Requires:   yum
Requires:   rpm
Provides:   Internet2-repo
Obsoletes:  Internet2-repo
Obsoletes:  Internet2-epel6-repo <= 0.1-1

%description
perfSONAR software release file. This package contains yum configuration for the perfSONAR RPM Repository, as well as the public GPG keys used to sign them.

%package nightly-patch
Summary:    perfSONAR nightly (patch version) repository
Group:      System Environment/Base
Provides:   Internet2-repo-nightly
Obsoletes:  Internet2-repo-nightly
Provides:   perfSONAR-repo-nightly
Obsoletes:  perfSONAR-repo-nightly

%description nightly-patch
Configures yum to use perfSONAR nightly repository for the next patch version

%package nightly-minor
Summary:    perfSONAR nightly (minor version) repository
Group:      System Environment/Base

%description nightly-minor
Configures yum to use perfSONAR nightly repository for the next minor version

%package staging
Summary:    perfSONAR staging repository
Group:      System Environment/Base
Provides:   Internet2-repo-staging
Obsoletes:  Internet2-repo-staging

%description staging
Configures yum to use perfSONAR staging repository

%package extras
Summary:    perfSONAR extras repository
Group:      System Environment/Base
Requires:   perfSONAR-repo
Provides:   Internet2-repo-extras
Obsoletes:  Internet2-repo-extras


%description extras
Configures yum to use perfSONAR extras repository


%prep
%setup -q -n perfSONAR-repo

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/etc/yum.repos.d
%{__cp} etc%{dist}/perfSONAR.repo $RPM_BUILD_ROOT/etc/yum.repos.d
%{__cp} etc%{dist}/perfSONAR-nightly-patch.repo $RPM_BUILD_ROOT/etc/yum.repos.d
%{__cp} etc%{dist}/perfSONAR-nightly-minor.repo $RPM_BUILD_ROOT/etc/yum.repos.d
%{__cp} etc%{dist}/perfSONAR-staging.repo $RPM_BUILD_ROOT/etc/yum.repos.d
%{__cp} etc%{dist}/perfSONAR-extras.repo $RPM_BUILD_ROOT/etc/yum.repos.d
%{__mkdir} -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg
%{__cp} etc%{dist}/RPM-GPG-KEY-perfSONAR $RPM_BUILD_ROOT/etc/pki/rpm-gpg
#These 3 are same key, but make copies so don't require any other packages to get key
%{__cp} etc%{dist}/RPM-GPG-KEY-perfSONAR-testing $RPM_BUILD_ROOT/etc/pki/rpm-gpg/RPM-GPG-KEY-perfSONAR-nightly-patch
%{__cp} etc%{dist}/RPM-GPG-KEY-perfSONAR-testing $RPM_BUILD_ROOT/etc/pki/rpm-gpg/RPM-GPG-KEY-perfSONAR-nightly-minor
%{__cp} etc%{dist}/RPM-GPG-KEY-perfSONAR-testing $RPM_BUILD_ROOT/etc/pki/rpm-gpg/RPM-GPG-KEY-perfSONAR-staging


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%config(noreplace) /etc/yum.repos.d/perfSONAR.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-perfSONAR

%files nightly-patch
%defattr(-, root, root, 0755)
%config(noreplace) /etc/yum.repos.d/perfSONAR-nightly-patch.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-perfSONAR-nightly-patch

%files nightly-minor
%defattr(-, root, root, 0755)
%config(noreplace) /etc/yum.repos.d/perfSONAR-nightly-minor.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-perfSONAR-nightly-minor

%files staging
%defattr(-, root, root, 0755)
%config(noreplace) /etc/yum.repos.d/perfSONAR-staging.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-perfSONAR-staging

%files extras
%defattr(-, root, root, 0755)
%config(noreplace) /etc/yum.repos.d/perfSONAR-extras.repo

%post
%if %{!?_without_rpmpubkey:1}0
rpm -q gpg-pubkey-9d7b9686-4947b567 &>/dev/null || rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-perfSONAR || :
rpm -q gpg-pubkey-242b3ccc-55816f7b &>/dev/null || rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-perfSONAR-testing || :
%endif

%changelog
* Mon Feb 11 2019 Andy Lake <andy@es.net> - 0.0.1-3
- Removed el6 support
- Removed web100 support
- Removed Vault
- Added nightly-patch and nightly-minor repos

* Thu Sep 30 2010 Aaron Brown <aaron@internet2.edu> - 0.0.1-3
- Remove apt-rpm support
- Add requirement on yum/rpm
- Add support for web100 kernel repository

* Thu Mar 26 2009 Jason Zurawski <zurawski@internet2.edu> - 0.0.1-2
- Update repo URLs.

* Thu Feb 12 2009 Jason Zurawski <zurawski@internet2.edu> - 0.0.1-1
- Initial package.

