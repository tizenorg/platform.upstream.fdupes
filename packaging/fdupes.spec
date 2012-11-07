#
# spec file for package fdupes (Version 1.40)
#
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           fdupes
Version:        1.40
Release:        42.66
License:        X11/MIT
Summary:        Identifying or deleting duplicate files
Url:            http://premium.caribe.net/~adrian2/fdupes.html
Group:          Productivity/Archiving/Compression
Source0:        %{name}-%{version}.tar.bz2
Source1:        macros.fdupes
Patch0:         %{name}.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FDUPES is a program for identifying or deleting duplicate files
residing within specified directories

%prep
%setup -q
%patch0

%build
make

%install
install -D -m755 fdupes %{buildroot}/usr/bin/fdupes
install -D -m644 fdupes.1 %{buildroot}/usr/share/man/man1/fdupes.1
install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.fdupes

%files
%defattr(-, root, root)
%doc CHANGES
%{_bindir}/fdupes
%{_mandir}/*/*
%{_sysconfdir}/rpm

