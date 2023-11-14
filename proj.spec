#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v2
# autospec commit: e661f3a625d7
#
Name     : proj
Version  : 9.3.0
Release  : 25
URL      : https://github.com/OSGeo/PROJ/releases/download/9.3.0/proj-9.3.0.tar.gz
Source0  : https://github.com/OSGeo/PROJ/releases/download/9.3.0/proj-9.3.0.tar.gz
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
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libnghttp2)
BuildRequires : pkgconfig(libssl)
BuildRequires : sqlite-autoconf-dev
BuildRequires : tiff-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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


%package doc
Summary: doc components for the proj package.
Group: Documentation
Requires: proj-man = %{version}-%{release}

%description doc
doc components for the proj package.


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
%setup -q -n proj-9.3.0
cd %{_builddir}/proj-9.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1700002314
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1700002314
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/proj
cp %{_builddir}/proj-%{version}/COPYING %{buildroot}/usr/share/package-licenses/proj/446797413e339410c98efdd33a006d5a4785fe1a || :
pushd clr-build
%make_install
popd
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
/usr/share/proj/triangulation.schema.json
/usr/share/proj/world

%files dev
%defattr(-,root,root,-)
/usr/include/geodesic.h
/usr/include/proj.h
/usr/include/proj/common.hpp
/usr/include/proj/coordinateoperation.hpp
/usr/include/proj/coordinates.hpp
/usr/include/proj/coordinatesystem.hpp
/usr/include/proj/crs.hpp
/usr/include/proj/datum.hpp
/usr/include/proj/io.hpp
/usr/include/proj/metadata.hpp
/usr/include/proj/nn.hpp
/usr/include/proj/util.hpp
/usr/include/proj_constants.h
/usr/include/proj_experimental.h
/usr/include/proj_symbol_rename.h
/usr/lib64/cmake/proj/proj-config-version.cmake
/usr/lib64/cmake/proj/proj-config.cmake
/usr/lib64/cmake/proj/proj-targets-relwithdebinfo.cmake
/usr/lib64/cmake/proj/proj-targets.cmake
/usr/lib64/cmake/proj/proj4-targets-relwithdebinfo.cmake
/usr/lib64/cmake/proj/proj4-targets.cmake
/usr/lib64/cmake/proj4/proj-targets-relwithdebinfo.cmake
/usr/lib64/cmake/proj4/proj-targets.cmake
/usr/lib64/cmake/proj4/proj4-config-version.cmake
/usr/lib64/cmake/proj4/proj4-config.cmake
/usr/lib64/cmake/proj4/proj4-targets-relwithdebinfo.cmake
/usr/lib64/cmake/proj4/proj4-targets.cmake
/usr/lib64/libproj.so
/usr/lib64/pkgconfig/proj.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/proj/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libproj.so.25
/usr/lib64/libproj.so.25.9.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/proj/446797413e339410c98efdd33a006d5a4785fe1a

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cct.1
/usr/share/man/man1/cs2cs.1
/usr/share/man/man1/geod.1
/usr/share/man/man1/gie.1
/usr/share/man/man1/proj.1
/usr/share/man/man1/projinfo.1
/usr/share/man/man1/projsync.1
