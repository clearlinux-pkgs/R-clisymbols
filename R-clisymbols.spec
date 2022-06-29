#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-clisymbols
Version  : 1.2.0
Release  : 32
URL      : https://cran.r-project.org/src/contrib/clisymbols_1.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/clisymbols_1.2.0.tar.gz
Summary  : Unicode Symbols at the R Prompt
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R

%description
when building command line applications. They fall back to
    alternatives on terminals that do not support Unicode.
    Many symbols were taken from the 'figures' 'npm' package

%prep
%setup -q -c -n clisymbols
cd %{_builddir}/clisymbols

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640989201

%install
export SOURCE_DATE_EPOCH=1640989201
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library clisymbols
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library clisymbols
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library clisymbols
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc clisymbols || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/clisymbols/DESCRIPTION
/usr/lib64/R/library/clisymbols/INDEX
/usr/lib64/R/library/clisymbols/LICENSE
/usr/lib64/R/library/clisymbols/Meta/Rd.rds
/usr/lib64/R/library/clisymbols/Meta/features.rds
/usr/lib64/R/library/clisymbols/Meta/hsearch.rds
/usr/lib64/R/library/clisymbols/Meta/links.rds
/usr/lib64/R/library/clisymbols/Meta/nsInfo.rds
/usr/lib64/R/library/clisymbols/Meta/package.rds
/usr/lib64/R/library/clisymbols/NAMESPACE
/usr/lib64/R/library/clisymbols/NEWS.md
/usr/lib64/R/library/clisymbols/R/clisymbols
/usr/lib64/R/library/clisymbols/R/clisymbols.rdb
/usr/lib64/R/library/clisymbols/R/clisymbols.rdx
/usr/lib64/R/library/clisymbols/README.markdown
/usr/lib64/R/library/clisymbols/help/AnIndex
/usr/lib64/R/library/clisymbols/help/aliases.rds
/usr/lib64/R/library/clisymbols/help/clisymbols.rdb
/usr/lib64/R/library/clisymbols/help/clisymbols.rdx
/usr/lib64/R/library/clisymbols/help/paths.rds
/usr/lib64/R/library/clisymbols/html/00Index.html
/usr/lib64/R/library/clisymbols/html/R.css
/usr/lib64/R/library/clisymbols/screenshot.png
/usr/lib64/R/library/clisymbols/tests/testthat.R
/usr/lib64/R/library/clisymbols/tests/testthat/test-all.R
