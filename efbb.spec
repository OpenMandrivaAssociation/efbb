%define gitdate 20150521

Summary:	Simple and robust network communication layer on top of UDP
Name:		efbb
Version:	%{gitdate}
Release:	0.1
Source0:	%{name}-%{version}.tar.xz
Patch0:		desktop-file.patch
Source100:	%{name}.rpmlintrc
License:	BSD
Group:		System/Libraries
URL:		https://git.enlightenment.org/games/efbb.git

BuildRequires:  edje
BuildRequires:  pkgconfig(elementary)
BuildRequires:  pkgconfig(evas)
BuildRequires:  pkgconfig(efl)
BuildRequires:  pkgconfig(edje)
BuildRequires:  pkgconfig(ephysics)
BuildRequires:  pkgconfig(etrophy)
BuildRequires:  pkgconfig(efreet)
BuildRequires:  pkgconfig(eina)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(enlightenment)
BuildRequires:	python-parsing
BuildRequires:	geneet


Requires:       e
Requires:	efl
Requires:	geneet

%description
Escape from Booty Bay is a physics game that explore EPhysics amazing features

%prep
%setup -qn %{name}
%apply_patches

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std


%files 
%{_libdir}/efbb_ql.so
%doc AUTHORS COPYING_FONTS COPYING_SOUNDS COPYING_ARTS INSTALL README TODO
%{_bindir}/*
%{_datadir}/efbb/*
%{_datadir}/applications/*
%{_datadir}/icons/*
