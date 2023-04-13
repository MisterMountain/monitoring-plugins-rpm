%global version 2.3.3
%global plugindir %{_libdir}/nagios/plugins

Name:           monitoring-plugins
Version:        2.3.3
Release:        1%{?dist}
Summary:        Monitoring Plugins from the Monitoring Plugins Team

License:        GPL3
URL:            https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz

##### REQUIREMENTS TO INSTALL ALL CHECK PLUGINS #####
Requires: %{name}-apt
Requires: %{name}-breeze
Requires: %{name}-by_ssh
Requires: %{name}-cluster
Requires: %{name}-curl
Requires: %{name}-dbi
Requires: %{name}-dhcp
Requires: %{name}-dig
Requires: %{name}-disk
Requires: %{name}-disk_smb
Requires: %{name}-dns
Requires: %{name}-dummy
Requires: %{name}-file_age
Requires: %{name}-flexlm
Requires: %{name}-fping
Requires: %{name}-hpjd
Requires: %{name}-http
Requires: %{name}-icmp
Requires: %{name}-ide_smart
Requires: %{name}-ifoperstatus
Requires: %{name}-ifstatus
Requires: %{name}-ircd
Requires: %{name}-ldap
Requires: %{name}-load
Requires: %{name}-log
Requires: %{name}-mailq
Requires: %{name}-mrtg
Requires: %{name}-mrtgtraf
Requires: %{name}-mysql
Requires: %{name}-mysql_query
Requires: %{name}-nagios
Requires: %{name}-nt
Requires: %{name}-ntp
Requires: %{name}-ntp_peer
Requires: %{name}-ntp_time
Requires: %{name}-nwstat
Requires: %{name}-oracle
Requires: %{name}-overcr
Requires: %{name}-pgsql
Requires: %{name}-ping
Requires: %{name}-procs
Requires: %{name}-radius
Requires: %{name}-real
Requires: %{name}-rpc
Requires: %{name}-sensors
Requires: %{name}-smtp
Requires: %{name}-snmp
Requires: %{name}-ssh
Requires: %{name}-swap
Requires: %{name}-tcp
Requires: %{name}-time
Requires: %{name}-ups
Requires: %{name}-uptime
Requires: %{name}-users
Requires: %{name}-wave



##### BUILD REQUIREMENTS #####

### General build requirements
BuildRequires: gcc
BuildRequires: make
BuildRequires: automake

### Check Plugin specific build requirements
# check_curl
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: uriparser-devel

# check_dbi
BuildRequires: libdbi-devel

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


%description
These are the Monitoring Plugins from the official Monitoring Plugins team



##### Sub Packages #####
# All

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
%{__make} install-root DESTDIR=%{buildroot} INSTALL="%{__install} -p" 

%clean
rm -rf %{buildroot}/*

%files
%doc ABOUT-NLS
%doc ACKNOWLEDGEMENTS
%doc AUTHORS
%doc CODING
%doc FAQ
%doc NEWS
%doc README
%doc README.md
%doc REQUIREMENTS
%doc SUPPORT
%license COPYING



# common
%package common
Summary: Monitoring Plugins - Common

%description common
Common files for Monitoring Plugins

%files common
%{plugindir}/negate
%{plugindir}/urlize
%{plugindir}/utils.pm
%{plugindir}/utils.sh
%doc ABOUT-NLS
%doc ACKNOWLEDGEMENTS
%doc AUTHORS
%doc CODING
%doc FAQ
%doc NEWS
%doc README
%doc README.md
%doc REQUIREMENTS
%doc SUPPORT
%license COPYING
/usr/share/locale/*/LC_MESSAGES/monitoring-plugins.mo



# check_apt
%package apt
Summary: Monitoring Plugins - check_apt
Requires: %{name}-common = %{version}-%{release}

%description apt
Provides check_apt of the Monitoring Plugins.

%files apt
%{plugindir}/check_apt



# check_breeze
%package breeze
Summary: Monitoring Plugins - check_breeze
Requires: %{name}-common = %{version}-%{release}

%description breeze
Provides check_breeze of the Monitoring Plugins.

%files breeze
%{plugindir}/check_breeze



# check_by_ssh
%package by_ssh
Summary: Monitoring Plugins - check_by_ssh
Requires: %{name}-common = %{version}-%{release}

%description by_ssh
Provides check_by_ssh of the Monitoring Plugins.

%files by_ssh
%{plugindir}/check_by_ssh



# check_cluster
%package cluster
Summary: Monitoring Plugins - check_cluster
Requires: %{name}-common = %{version}-%{release}

%description cluster
Provides check_cluster of the Monitoring Plugins.

%files cluster
%{plugindir}/check_cluster



# check_curl
%package curl
Summary: Monitoring Plugins - check_curl
Requires: %{name}-common = %{version}-%{release}

%description curl
Provides check_curl of the Monitoring Plugins.

%files curl
%{plugindir}/check_curl



# check_dbi
%package dbi
Summary: Monitoring Plugins - check_dbi
Requires: %{name}-common = %{version}-%{release}

%description dbi
Provides check_dbi of the Monitoring Plugins.

%files dbi
%{plugindir}/check_dbi



# check_dhcp
%package dhcp
Summary: Monitoring Plugins - check_dhcp
Requires: %{name}-common = %{version}-%{release}

%description dhcp
Provides check_dhcp of the Monitoring Plugins.

%files dhcp
%{plugindir}/check_dhcp



# check_dig
%package dig
Summary: Monitoring Plugins - check_dig
Requires: %{name}-common = %{version}-%{release}
Recommends: bind-utils

%description dig
Provides check_dig of the Monitoring Plugins.

%files dig
%{plugindir}/check_dig



# check_disk
%package disk
Summary: Monitoring Plugins - check_disk
Requires: %{name}-common = %{version}-%{release}

%description disk
Provides check_disk of the Monitoring Plugins.

%files disk
%{plugindir}/check_disk



# check_disk_smb
%package disk_smb
Summary:    Monitoring Plugins - check_disk_smb
Requires:   %{name}-common = %{version}-%{release}
Recommends: samba-client

%description disk_smb
Provides check_disk_smb of the Monitoring Plugins.

%files disk_smb
%{plugindir}/check_disk_smb



# check_dns
%package dns
Summary:    Monitoring Plugins - check_dns
Requires:   %{name}-common = %{version}-%{release}
Recommends: bind-utils

%description dns
Provides check_dns of the Monitoring Plugins.

%files dns
%{plugindir}/check_dns



# check_dummy
%package dummy
Summary:    Monitoring Plugins - check_dummy
Requires:   %{name}-common = %{version}-%{release}

%description dummy
Provides check_dummy of the Monitoring Plugins.

%files dummy
%{plugindir}/check_dummy



# check_file_age
%package file_age
Summary:    Monitoring Plugins - check_file_age
Requires:   %{name}-common = %{version}-%{release}

%description file_age
Provides check_file_age of the Monitoring Plugins.

%files file_age
%{plugindir}/check_file_age



# check_flexlm
%package flexlm
Summary:    Monitoring Plugins - check_flexlm
Requires:   %{name}-common = %{version}-%{release}

%description flexlm
Provides check_flexlm of the Monitoring Plugins.

%files flexlm
%{plugindir}/check_flexlm



# check_fping
%package fping
Summary:    Monitoring Plugins - check_fping
Requires:   %{name}-common = %{version}-%{release}

%description fping
Provides check_fping of the Monitoring Plugins.

%files fping
%{plugindir}/check_fping



# check_hpjd
%package hpjd
Summary:    Monitoring Plugins - check_hpjd
Requires:   %{name}-common = %{version}-%{release}

%description hpjd
Provides check_hpjd of the Monitoring Plugins.

%files hpjd
%{plugindir}/check_hpjd



# check_http
%package http
Summary:    Monitoring Plugins - check_http
Requires:   %{name}-common = %{version}-%{release}

%description http
Provides check_http of the Monitoring Plugins.

%files http
%{plugindir}/check_http



# check_icmp
%package icmp
Summary:    Monitoring Plugins - check_icmp
Requires:   %{name}-common = %{version}-%{release}

%description icmp
Provides check_icmp of the Monitoring Plugins.

%files icmp
%{plugindir}/check_icmp



# check_ide_smart
%package ide_smart
Summary:    Monitoring Plugins - check_ide_smart
Requires:   %{name}-common = %{version}-%{release}

%description ide_smart
Provides check_ide_smart of the Monitoring Plugins.

%files ide_smart
%{plugindir}/check_ide_smart



# check_ifoperstatus
%package ifoperstatus
Summary:    Monitoring Plugins - check_ifoperstatus
Requires:   %{name}-common = %{version}-%{release}
Recommends: perl(Net::SNMP)

%description ifoperstatus
Provides check_ifoperstatus of the Monitoring Plugins.

%files ifoperstatus
%{plugindir}/check_ifoperstatus



# check_ifstatus
%package ifstatus
Summary:    Monitoring Plugins - check_ifstatus
Requires:   %{name}-common = %{version}-%{release}

%description ifstatus
Provides check_ifstatus of the Monitoring Plugins.

%files ifstatus
%{plugindir}/check_ifstatus



# check_ircd
%package ircd
Summary:    Monitoring Plugins - check_ircd
Requires:   %{name}-common = %{version}-%{release}

%description ircd
Provides check_ircd of the Monitoring Plugins.

%files ircd
%{plugindir}/check_ircd



# check_ldap
%package ldap
Summary:    Monitoring Plugins - check_ldap
Requires:   %{name}-common = %{version}-%{release}

%description ldap
Provides check_ldap of the Monitoring Plugins.

%files ldap
%{plugindir}/check_ldap
%{plugindir}/check_ldaps



# check_load
%package load
Summary:    Monitoring Plugins - check_load
Requires:   %{name}-common = %{version}-%{release}

%description load
Provides check_load of the Monitoring Plugins.

%files load
%{plugindir}/check_load



# check_log
%package log
Summary:    Monitoring Plugins - check_log
Requires:   %{name}-common = %{version}-%{release}

%description log
Provides check_log of the Monitoring Plugins.

%files log
%{plugindir}/check_log



# check_mailq
%package mailq
Summary:    Monitoring Plugins - check_mailq
Requires:   %{name}-common = %{version}-%{release}

%description mailq
Provides check_mailq of the Monitoring Plugins.

%files mailq
%{plugindir}/check_mailq



# check_mrtg
%package mrtg
Summary:    Monitoring Plugins - check_mrtg
Requires:   %{name}-common = %{version}-%{release}

%description mrtg
Provides check_mrtg of the Monitoring Plugins.

%files mrtg
%{plugindir}/check_mrtg



# check_mrtgtraf
%package mrtgtraf
Summary:    Monitoring Plugins - check_mrtgtraf
Requires:   %{name}-common = %{version}-%{release}

%description mrtgtraf
Provides check_mrtgtraf of the Monitoring Plugins.

%files mrtgtraf
%{plugindir}/check_mrtgtraf



# check_mysql
%package mysql
Summary:    Monitoring Plugins - check_mysql
Requires:   %{name}-common = %{version}-%{release}

%description mysql
Provides check_mysql of the Monitoring Plugins.

%files mysql
%{plugindir}/check_mysql



# check_mysql_query
%package mysql_query
Summary:    Monitoring Plugins - check_mysql_query
Requires:   %{name}-common = %{version}-%{release}

%description mysql_query
Provides check_mysql_query of the Monitoring Plugins.

%files mysql_query
%{plugindir}/check_mysql_query



# check_nagios
%package nagios
Summary:    Monitoring Plugins - check_nagios
Requires:   %{name}-common = %{version}-%{release}

%description nagios
Provides check_nagios of the Monitoring Plugins.

%files nagios
%{plugindir}/check_nagios



# check_nt
%package nt
Summary:    Monitoring Plugins - check_nt
Requires:   %{name}-common = %{version}-%{release}

%description nt
Provides check_nt of the Monitoring Plugins.

%files nt
%{plugindir}/check_nt



# check_ntp
%package ntp
Summary:    Monitoring Plugins - check_ntp
Requires:   %{name}-common = %{version}-%{release}

%description ntp
Provides check_ntp of the Monitoring Plugins.

%files ntp
%{plugindir}/check_ntp



# check_ntp_peer
%package ntp_peer
Summary:    Monitoring Plugins - check_ntp_peer
Requires:   %{name}-common = %{version}-%{release}

%description ntp_peer
Provides check_ntp_peer of the Monitoring Plugins.

%files ntp_peer
%{plugindir}/check_ntp_peer



# check_ntp_time
%package ntp_time
Summary:    Monitoring Plugins - check_ntp_time
Requires:   %{name}-common = %{version}-%{release}

%description ntp_time
Provides check_ntp_time of the Monitoring Plugins.

%files ntp_time
%{plugindir}/check_ntp_time



# check_nwstat
%package nwstat
Summary:    Monitoring Plugins - check_nwstat
Requires:   %{name}-common = %{version}-%{release}

%description nwstat
Provides check_nwstat of the Monitoring Plugins.

%files nwstat
%{plugindir}/check_nwstat



# check_oracle
%package oracle
Summary:    Monitoring Plugins - check_oracle
Requires:   %{name}-common = %{version}-%{release}

%description oracle
Provides check_oracle of the Monitoring Plugins.

%files oracle
%{plugindir}/check_oracle



# check_overcr
%package overcr
Summary:    Monitoring Plugins - check_overcr
Requires:   %{name}-common = %{version}-%{release}

%description overcr
Provides check_overcr of the Monitoring Plugins.

%files overcr
%{plugindir}/check_overcr



# check_pgsql
%package pgsql
Summary:    Monitoring Plugins - check_pgsql
Requires:   %{name}-common = %{version}-%{release}

%description pgsql
Provides check_pgsql of the Monitoring Plugins.

%files pgsql
%{plugindir}/check_pgsql



# check_ping
%package ping
Summary:    Monitoring Plugins - check_ping
Requires:   %{name}-common = %{version}-%{release}

%description ping
Provides check_ping of the Monitoring Plugins.

%files ping
%{plugindir}/check_ping



# check_procs
%package procs
Summary:    Monitoring Plugins - check_procs
Requires:   %{name}-common = %{version}-%{release}

%description procs
Provides check_procs of the Monitoring Plugins.

%files procs
%{plugindir}/check_procs



# check_radius
%package radius
Summary:    Monitoring Plugins - check_radius
Requires:   %{name}-common = %{version}-%{release}

%description radius
Provides check_radius of the Monitoring Plugins.

%files radius
%{plugindir}/check_radius



# check_real
%package real
Summary:    Monitoring Plugins - check_real
Requires:   %{name}-common = %{version}-%{release}

%description real
Provides check_real of the Monitoring Plugins.

%files real
%{plugindir}/check_real



# check_rpc
%package rpc
Summary:    Monitoring Plugins - check_rpc
Requires:   %{name}-common = %{version}-%{release}

%description rpc
Provides check_rpc of the Monitoring Plugins.

%files rpc
%{plugindir}/check_rpc



# check_sensors
%package sensors
Summary:    Monitoring Plugins - check_sensors
Requires:   %{name}-common = %{version}-%{release}

%description sensors
Provides check_sensors of the Monitoring Plugins.

%files sensors
%{plugindir}/check_sensors



# check_smtp
%package smtp
Summary:    Monitoring Plugins - check_smtp
Requires:   %{name}-common = %{version}-%{release}

%description smtp
Provides check_smtp of the Monitoring Plugins.

%files smtp
%{plugindir}/check_smtp



# check_snmp
%package snmp
Summary:    Monitoring Plugins - check_snmp
Requires:   %{name}-common = %{version}-%{release}
Recommends: net-snmp

%description snmp
Provides check_snmp of the Monitoring Plugins.

%files snmp
%{plugindir}/check_snmp



# check_ssh
%package ssh
Summary:    Monitoring Plugins - check_ssh
Requires:   %{name}-common = %{version}-%{release}

%description ssh
Provides check_ssh of the Monitoring Plugins.

%files ssh
%{plugindir}/check_ssh



# check_swap
%package swap
Summary:    Monitoring Plugins - check_swap
Requires:   %{name}-common = %{version}-%{release}

%description swap
Provides check_swap of the Monitoring Plugins.

%files swap
%{plugindir}/check_swap



# check_tcp
%package tcp
Summary:    Monitoring Plugins - check_tcp
Requires:   %{name}-common = %{version}-%{release}

%description tcp
Provides check_tcp of the Monitoring Plugins.

%files tcp
%{plugindir}/check_clamd
%{plugindir}/check_ftp
%{plugindir}/check_imap
%{plugindir}/check_jabber
%{plugindir}/check_nntp
%{plugindir}/check_nntps
%{plugindir}/check_pop
%{plugindir}/check_simap
%{plugindir}/check_spop
%{plugindir}/check_ssmtp
%{plugindir}/check_tcp
%{plugindir}/check_udp



# check_time
%package time
Summary:    Monitoring Plugins - check_time
Requires:   %{name}-common = %{version}-%{release}

%description time
Provides check_time of the Monitoring Plugins.

%files time
%{plugindir}/check_time



# check_ups
%package ups
Summary:    Monitoring Plugins - check_ups
Requires:   %{name}-common = %{version}-%{release}

%description ups
Provides check_ups of the Monitoring Plugins.

%files ups
%{plugindir}/check_ups



# check_uptime
%package uptime
Summary:    Monitoring Plugins - check_uptime
Requires:   %{name}-common = %{version}-%{release}

%description uptime
Provides check_uptime of the Monitoring Plugins.

%files uptime
%{plugindir}/check_uptime



# check_users
%package users
Summary:    Monitoring Plugins - check_users
Requires:   %{name}-common = %{version}-%{release}

%description users
Provides check_users of the Monitoring Plugins.

%files users
%{plugindir}/check_users



# check_wave
%package wave
Summary:    Monitoring Plugins - check_wave
Requires:   %{name}-common = %{version}-%{release}

%description wave
Provides check_wave of the Monitoring Plugins.

%files wave
%{plugindir}/check_wave
