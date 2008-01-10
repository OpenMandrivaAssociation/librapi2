%define name	librapi2
%define shortname rapi
%define release  %mkrel 1
%define version  0.11

%define major 2

%define libname %mklibname %shortname %major

Summary: SynCE: Remote Application Programming Interface (RAPI) library
Name: %{name}
Version: %{version}
Release: %{release}
License: MIT
Group: System/Libraries
Source: %{name}-%{version}.tar.bz2
URL: http://synce.sourceforge.net/
Buildroot: %{_tmppath}/%name-root
BuildRequires: libsynce-devel = %{version}
BuildRequires: python-devel
BuildRequires: python-pyrex
Conflicts: synce < 0.9.3
Obsoletes: synce-%libname
Obsoletes: %libname < %libname-%{version}

%description
Librapi is part of the SynCE project:

  http://synce.sourceforge.net/

The RAPI library is an open source implementation that works like RAPI.DLL,
available on Microsoft operating systems. The library makes it possible to make
remote calls to a computer running Pocket PC. Documentation for the RAPI calls
is available at this address:

http://msdn.microsoft.com/library/default.asp?url=/library/en-us/wcesdkr/htm/_wcesdk_CeRapiInit.asp

%package -n %libname-python
Group: System/Libraries
Summary: SynCE: Remote Application Programming Interface (RAPI) library
Provides: %{shortname}-python = %{version}-%{release}
Provides: lib%{shortname}-python = %{version}-%{release}
Requires: %{libname} = %{version}-%{release}
Requires: python
Obsoletes: %libname-python < %libname-python-%{version}

%description -n %libname-python
Librapi is part of the SynCE project:

  http://synce.sourceforge.net/

The RAPI library is an open source implementation that works like RAPI.DLL,
available on Microsoft operating systems. The library makes it possible to make
remote calls to a computer running Pocket PC. Documentation for the RAPI calls
is available at this address:

http://msdn.microsoft.com/library/default.asp?url=/library/en-us/wcesdkr/htm/_wcesdk_CeRapiInit.asp


%package -n %libname-devel
Group: System/Libraries
Summary: SynCE: Remote Application Programming Interface (RAPI) library
Provides: lib%{shortname}-devel = %{version}-%{release}
Requires: %{libname} = %{version}-%{release}
Conflicts: %{_lib}synce0-devel < 0.9.3
Obsoletes: %libname-devel < %libname-devel-%{version}

%description -n %libname-devel
Librapi is part of the SynCE project:

  http://synce.sourceforge.net/

The RAPI library is an open source implementation that works like RAPI.DLL,
available on Microsoft operating systems. The library makes it possible to make
remote calls to a computer running Pocket PC. Documentation for the RAPI calls
is available at this address:

http://msdn.microsoft.com/library/default.asp?url=/library/en-us/wcesdkr/htm/_wcesdk_CeRapiInit.asp

%prep
%setup -q -n %{libname}-%{version}

%build
%configure2_5x --with-libsynce=%{_prefix}
%make

%install
rm -rf %buildroot
%makeinstall_std

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README TODO
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%_libdir/librapi.so.%{major}
%_libdir/librapi.so.%{major}.*

%files -n %{libname}-devel
%defattr(-,root,root)
%_libdir/librapi.so
%_libdir/librapi.a
%_libdir/librapi.la
%{_includedir}/rapi.h
%_libdir/pkgconfig/*.pc

%files -n %{libname}-python
%python_sitearch/pyrapi2.*
