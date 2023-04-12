%global version 2.3.3
%global plugindir %{_libdir}/nagios/plugins

Name:           monitoring-plugins
Version:        2.3.3
Release:        1%{?dist}
Summary:        Monitoring Plugins from the Monitoring Plugins Team

License:        GPL3
URL:            https://github.com/monitoring-plugins/monitoring-plugins
Source0:        https://github.com/monitoring-plugins/monitoring-plugins/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  automake

BuildRequires:  bind-utils
BuildRequires:  fping
BuildRequires:  libcurl-devel
BuildRequires:  mysql-devel
BuildRequires:  net-snmp
BuildRequires:  net-snmp-utils
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  postgresql-devel
BuildRequires:  radcli-devel
BuildRequires:  samba-client
BuildRequires:  uriparser-devel

%if 0%{?rhel} == 8
BuildRequires: libdbi-devel
%endif

#### Wegen qstat/check_game (pseudo code)
#%%if 0%{?EL VERSION} == 8
#BuildRequires:  qstat
#%%endif
####

Recommends:     net-snmp
Recommends:     net-snmp-utils
Recommends:     perl(Net::SNMP)
Recommends:     samba-client
Recommends:     bind-utils

%description
These are the monitoring plugins from the official monitoring plugins team

%prep
%autosetup
./tools/setup

%build
./configure \
    --prefix=%{_prefix} \
    --libexecdir=%{plugindir} \
    --with-perl=/usr/bin/perl
%make_build

%install
%make_install
%{__make} install-root DESTDIR=%{?buildroot} INSTALL="%{__install} -p"


%clean
rm -rf %{_buildrootdir}/*

%files
%{plugindir}/*
/usr/share/locale/*/LC_MESSAGES/monitoring-plugins.mo

#%%doc

#%%changelog
