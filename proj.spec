#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : proj
Version  : 7.1.1
Release  : 15
URL      : http://download.osgeo.org/proj/proj-7.1.1.tar.gz
Source0  : http://download.osgeo.org/proj/proj-7.1.1.tar.gz
Summary  : Coordinate transformation software library
Group    : Development/Tools
License  : MIT
Requires: proj-bin = %{version}-%{release}
Requires: proj-data = %{version}-%{release}
Requires: proj-lib = %{version}-%{release}
Requires: proj-license = %{version}-%{release}
Requires: proj-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : pkgconfig(gtest)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libnghttp2)
BuildRequires : pkgconfig(libssl)
BuildRequires : pkgconfig(libtiff-4)
BuildRequires : pkgconfig(sqlite3)

%description
# PROJ
PROJ is a generic coordinate transformation software, that transforms
coordinates from one coordinate reference system (CRS) to another.
This includes cartographic projections as well as geodetic transformations.

%package bin
Summary: bin components for the proj package.
Group: Binaries
Requires: proj-data = %{version}-%{release}
Requires: proj-license = %{version}-%{release}

%description bin
bin components for the proj package.


%package data
Summary: data components for the proj package.
Group: Data

%description data
data components for the proj package.


%package dev
Summary: dev components for the proj package.
Group: Development
Requires: proj-lib = %{version}-%{release}
Requires: proj-bin = %{version}-%{release}
Requires: proj-data = %{version}-%{release}
Provides: proj-devel = %{version}-%{release}
Requires: proj = %{version}-%{release}

%description dev
dev components for the proj package.


%package lib
Summary: lib components for the proj package.
Group: Libraries
Requires: proj-data = %{version}-%{release}
Requires: proj-license = %{version}-%{release}

%description lib
lib components for the proj package.


%package license
Summary: license components for the proj package.
Group: Default

%description license
license components for the proj package.


%package man
Summary: man components for the proj package.
Group: Default

%description man
man components for the proj package.


%prep
%setup -q -n proj-7.1.1
cd %{_builddir}/proj-7.1.1
pushd ..
cp -a proj-7.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598975438
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --enable-lto
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export FFLAGS="$FFLAGS -m64 -march=haswell"
export FCFLAGS="$FCFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static --enable-lto
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1598975438
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/proj
cp %{_builddir}/proj-7.1.1/COPYING %{buildroot}/usr/share/package-licenses/proj/ff8d569976b75bad2e71d78ad1df7a422f1165c9
pushd ../buildavx2/
%make_install_avx2
popd
%make_install
## install_append content
# Set the database journal mode away from WAL so it can be queried read-only
/usr/bin/sqlite3 %{buildroot}/usr/share/proj/proj.db 'PRAGMA journal_mode=DELETE;'
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cct
/usr/bin/cs2cs
/usr/bin/geod
/usr/bin/gie
/usr/bin/haswell/cct
/usr/bin/haswell/cs2cs
/usr/bin/haswell/geod
/usr/bin/haswell/gie
/usr/bin/haswell/invgeod
/usr/bin/haswell/invproj
/usr/bin/haswell/proj
/usr/bin/haswell/projinfo
/usr/bin/haswell/projsync
/usr/bin/invgeod
/usr/bin/invproj
/usr/bin/proj
/usr/bin/projinfo
/usr/bin/projsync

%files data
%defattr(-,root,root,-)
/usr/share/proj/CH
/usr/share/proj/GL27
/usr/share/proj/ITRF2000
/usr/share/proj/ITRF2008
/usr/share/proj/ITRF2014
/usr/share/proj/deformation_model.schema.json
/usr/share/proj/nad.lst
/usr/share/proj/nad27
/usr/share/proj/nad83
/usr/share/proj/other.extra
/usr/share/proj/proj.db
/usr/share/proj/proj.ini
/usr/share/proj/projjson.schema.json
/usr/share/proj/world

%files dev
%defattr(-,root,root,-)
/usr/include/geodesic.h
/usr/include/proj.h
/usr/include/proj/common.hpp
/usr/include/proj/coordinateoperation.hpp
/usr/include/proj/coordinatesystem.hpp
/usr/include/proj/crs.hpp
/usr/include/proj/datum.hpp
/usr/include/proj/io.hpp
/usr/include/proj/metadata.hpp
/usr/include/proj/nn.hpp
/usr/include/proj/util.hpp
/usr/include/proj_api.h
/usr/include/proj_constants.h
/usr/include/proj_experimental.h
/usr/include/proj_symbol_rename.h
/usr/lib64/haswell/libproj.so
/usr/lib64/libproj.so
/usr/lib64/pkgconfig/proj.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libproj.so.19
/usr/lib64/haswell/libproj.so.19.1.1
/usr/lib64/libproj.so.19
/usr/lib64/libproj.so.19.1.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/proj/ff8d569976b75bad2e71d78ad1df7a422f1165c9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cct.1
/usr/share/man/man1/cs2cs.1
/usr/share/man/man1/geod.1
/usr/share/man/man1/gie.1
/usr/share/man/man1/proj.1
/usr/share/man/man1/projinfo.1
/usr/share/man/man1/projsync.1
