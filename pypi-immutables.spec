#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-immutables
Version  : 0.19
Release  : 12
URL      : https://files.pythonhosted.org/packages/c3/bf/113933c9d098c58cee52c68a205cd449bcc331c32156267d337125780bf6/immutables-0.19.tar.gz
Source0  : https://files.pythonhosted.org/packages/c3/bf/113933c9d098c58cee52c68a205cd449bcc331c32156267d337125780bf6/immutables-0.19.tar.gz
Summary  : Immutable Collections
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-immutables-filemap = %{version}-%{release}
Requires: pypi-immutables-lib = %{version}-%{release}
Requires: pypi-immutables-license = %{version}-%{release}
Requires: pypi-immutables-python = %{version}-%{release}
Requires: pypi-immutables-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
immutables
==========
.. image:: https://github.com/MagicStack/immutables/workflows/Tests/badge.svg?branch=master
:target: https://github.com/MagicStack/immutables/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush

%package filemap
Summary: filemap components for the pypi-immutables package.
Group: Default

%description filemap
filemap components for the pypi-immutables package.


%package lib
Summary: lib components for the pypi-immutables package.
Group: Libraries
Requires: pypi-immutables-license = %{version}-%{release}
Requires: pypi-immutables-filemap = %{version}-%{release}

%description lib
lib components for the pypi-immutables package.


%package license
Summary: license components for the pypi-immutables package.
Group: Default

%description license
license components for the pypi-immutables package.


%package python
Summary: python components for the pypi-immutables package.
Group: Default
Requires: pypi-immutables-python3 = %{version}-%{release}

%description python
python components for the pypi-immutables package.


%package python3
Summary: python3 components for the pypi-immutables package.
Group: Default
Requires: pypi-immutables-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(immutables)

%description python3
python3 components for the pypi-immutables package.


%prep
%setup -q -n immutables-0.19
cd %{_builddir}/immutables-0.19
pushd ..
cp -a immutables-0.19 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663201232
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-immutables
cp %{_builddir}/immutables-%{version}/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/pypi-immutables/ad35a1f361b4d6c956a59710f3b88965da9d0792 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-immutables

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-immutables/ad35a1f361b4d6c956a59710f3b88965da9d0792

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
