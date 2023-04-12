%global version 2.3.3
%global plugindir %{_libdir}/nagios/plugins

Name:           monitoring-plugins
Version:        2.3.3
Release:        1%{?dist}
Summary:        Monitoring Plugins from the Monitoring Plugins Team

License:        GPL3
URL:            https://github.com/monitoring-plugins/monitoring-plugins
Source0:        https://github.com/monitoring-plugins/monitoring-plugins/archive/v%{version}.tar.gz



##### BUILD REQUIREMENTS #####

### General build requirements
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  automake

### Check Plugin specific build requirements
# check_curl
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel
BuildRequires:  uriparser-devel

# check_dbi
BuildRequires:  libdbi-devel

# check_dig check_dns
BuildRequires: bind-utils

# check_disk_smb
BuildRequires: samba-client

# check_fping
BuildRequires: fping

# check_hpjd
BuildRequires: net-snmp-utils

# check_ldap check_ldaps
BuildRequires: openldap-devel

# check_mysql check_mysql_query
BuildRequires: mysql-devel

# check_pgsql
BuildRequires: postgresql-devel

# check_radius
BuildRequires: radcli-devel



##### RUNTIME REQUIREMENTS / RECOMMENDATIONS #####

# check_dig check_dns
Recommends: bind-utils

# check_disk_smb
Recommends: samba-client

# check_ifoperstatus
Recommends: perl(Net::SNMP)

# check_snmp
Recommends: net-snmp
#Requires:
Recommends:     net-snmp
Recommends:     net-snmp-utils
Recommends:     perl(Net::SNMP)
Recommends:     samba-client


%description
These are the monitoring plugins from the official monitoring plugins team

##### Sub Packages #####
# All
%package all

Summary: Nagios Plugins - All plugins
Requires: monitoring-plugins-apt
%description all
This package provides all Nagios plugins.


# check_apt
%package apt

Summary: Nagios Plugin - check_apt
Requires: monitoring-plugins = %{version}-%{release}
%description apt
Provides check_apt support for Nagios.



#%%description
#These are the monitoring plugins from the official monitoring plugins team


%prep
%autosetup
./tools/setup

%build
./configure \
    --prefix=%{_prefix} \
    --libexecdir=%{plugindir} \
    --with-openssl=yes \
    --with-ping-command="/usr/bin/ping -4 -n -U -w %d -c %d %s" \
    --with-ping6-command="/usr/bin/ping -6 -n -U -w %d -c %d %s"
%make_build

%install
%make_install
%{__make} install-root DESTDIR=%{?buildroot} INSTALL="%{__install} -p"

#%%clean
#rm -rf %{_buildrootdir}/*

%files
#%%{plugindir}/*
/usr/share/locale/*/LC_MESSAGES/monitoring-plugins.mo


%files apt
%{plugindir}/check_apt

#%%doc

#%%changelog
