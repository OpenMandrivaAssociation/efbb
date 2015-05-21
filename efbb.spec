#%define major 7
#%define libname %mklibname %{name} %{major}
#%define develname %mklibname %{name} -d
%define gitdate 20150521

Summary:	Simple and robust network communication layer on top of UDP
Name:		efbb
Version:	%{gitdate}
Release:	0.1
Source0:	%{name}-%{version}.tar.xz
#Source100:	enet.rpmlintrc
License:	BSD
Group:		System/Libraries
URL:		https://git.enlightenment.org/games/efbb.git

BuildRequires:  edje
#BuildRequires:  embryo
BuildRequires:  pkgconfig(elementary)
BuildRequires:  pkgconfig(evas)
BuildRequires:  pkgconfig(ecore)
BuildRequires:  pkgconfig(edje)
BuildRequires:  pkgconfig(ephysics)
BuildRequires:  pkgconfig(etrophy)
BuildRequires:  pkgconfig(efreet)
BuildRequires:  pkgconfig(eina)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(enlightenment)

Requires:       e

%description
Escape from Booty Bay is a physics game that explore EPhysics amazing features

#%package -n	%{libname}
#Summary:	Libraries for %{name}
#Group:		System/Libraries

#%description -n	%{libname}
#ENet's purpose is to provide a relatively thin, simple and robust
#network communication layer on top of UDP (User Datagram Protocol). The
#primary feature it provides is optional reliable, in-order delivery of
#packets.

#ENet omits certain higher level networking features such as
#authentication, lobbying, server discovery, encryption, or other similar
#tasks that are particularly application specific so that the library
#remains flexible, portable, and easily embeddable.

#This package provides the libraries for %{name}.

#%package -n %{develname}
#Summary:	Development files for for %{name}
#Group:		Development/C
#Requires:	%{libname} = %{version}-%{release}
#Provides:	%{name}-devel = %{version}-%{release}
#Provides:	lib%{name}-devel = %{version}-%{release}

#%description -n	%{develname}
#Development files and headers for %{name}.

%prep
%setup -qn %{name}

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

# we don't want	these
#rm -rf %{buildroot}%{_libdir}/*.la

%files 
%{_libdir}/libenet.so.%{major}*
%doc LICENSE README ChangeLog
%{_includedir}/%{name}
%{_bindir}/*
%{_libdir}/pkgconfig/libenet.pc
