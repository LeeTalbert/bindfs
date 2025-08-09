%global debug_package %{nil}

Name:		bindfs
Version:	1.18.1
Release:	1
Source0:	https://github.com/mpartel/bindfs/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	FUSE filesystem for mirroring a directory to another directory
URL:		https://github.com/mpartel/bindfs
License:	GPL
Group:		File Tools

BuildRequires:	make
BuildRequires:  lib64fuse3-devel

%description
FUSE filesystem for mirroring a directory to another directory, similarly to mount --bind. The permissions of the mirrored directory can be altered in various ways.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
